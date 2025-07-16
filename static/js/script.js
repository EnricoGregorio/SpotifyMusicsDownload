function showLoadingMessage() {
    document.getElementById('loading').style.display = 'block'
}

function changeBgColor(color) {
    let colorMode = color;
    const COR_PRETA = 'var(--cor0)';
    const COR_CLARA = 'var(--cor1)';

    if (colorMode === 'dark') {
        document.getElementById('dark-mode').style.display = 'none'
        document.getElementById('light-mode').style.display = 'block'

        document.getElementById('page').style.backgroundColor = COR_CLARA
        document.querySelector("p").style.color = COR_PRETA
        document.querySelector("h1").style.color = COR_PRETA
        document.querySelector("label").style.color = COR_PRETA
        document.getElementById("message").style.color = COR_PRETA
    } else {
        document.getElementById('dark-mode').style.display = 'block'
        document.getElementById('light-mode').style.display = 'none'

        document.getElementById('page').style.backgroundColor = COR_PRETA
        document.querySelector("p").style.color = COR_CLARA
        document.querySelector("h1").style.color = COR_CLARA
        document.querySelector("label").style.color = COR_CLARA
        document.getElementById("message").style.color = COR_CLARA

    }
}