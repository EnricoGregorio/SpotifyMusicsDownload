import os
from flask import Flask, render_template, request # type: ignore
import subprocess

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
                # Garante que a pasta existe.
                os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

                # Comando com diretório de saída.
                subprocess.run([
                    'spotdl',
                    playlistURL,
                    '--output',
                    os.path.join(DOWNLOAD_FOLDER, '{title} - {artist}') # Como a(s) música(s) será/serão nomeada(s) e em que pasta elas serão salvas.
                    ], check=True)
                
                mensagem = f"Download realizado com sucesso! Basta abrir a pasta <strong>musics</strong> para visualizar o(s) arquivo(s)."
            except subprocess.CalledProcessError as e:
                mensagem = f"Ocorreu um erro: {e}"
    return render_template("index.html", resultado=mensagem)