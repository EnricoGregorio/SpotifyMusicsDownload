import os
from flask import Flask, render_template, request, send_file # type: ignore
import subprocess, os, tempfile, zipfile, shutil

app = Flask(__name__)

# Caminho absoluto para a pasta de musics.
DOWNLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'musics')

@app.route("/", methods=['GET','POST'])
def index():
    mensagem = None

    if request.method == "POST":
        playlistURL = request.form['link']
        if playlistURL:
            try:
                # Cria um diretório temporário para o download
                temp_dir = tempfile.mkdtemp()
                subprocess.run([
                    'spotdl', playlistURL,
                    '--output', os.path.join(temp_dir, '{title} - {artist}')
                ], check=True)

                # Pega o primeiro arquivo baixado
                arquivos = os.listdir(temp_dir)
                if not arquivos:
                    mensagem = "Nenhum arquivo foi baixado."
                    return render_template('index.html', mensagem=mensagem)
                
                # Se for apenas 1 música, então baixa direto
                if len(arquivos) == 1:
                    caminho_arquivo = os.path.join(temp_dir, arquivos[0])
                    return send_file(
                        caminho_arquivo,
                        as_attachment=True,
                        download_name=arquivos[0]
                    )

                # Se for mais de 1 música, então cria um ZIP
                zip_path = os.path.join(temp_dir, 'musicas.zip')
                with zipfile.ZipFile(zip_path, 'w') as zipf:
                    for nome_arquivo in arquivos:
                        caminho = os.path.join(temp_dir, nome_arquivo)
                        zipf.write(caminho, arcname=nome_arquivo)

                # Envia o ZIP para o navegador
                return send_file(
                    zip_path,
                    as_attachment=True,
                    download_name='musicas_spotify.zip'
                )
            
            except subprocess.CalledProcessError as e:
                mensagem = f"Ocorreu um erro ao baixar: {e}"
            finally:
                mensagem = "Música(s) baixada(s)!"
                # Remove os arquivos temporários após o envio
                try:
                    shutil.rmtree(temp_dir)
                except Exception:
                    pass
        
    return render_template("index.html", resultado=mensagem)