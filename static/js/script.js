function showLoadingMessage() {
    document.getElementById('loading').style.display = 'block'
}

function changeBgColor(color) {
    let colorMode = color;
    const COR0 = 'var(--cor0)';
    const COR1 = 'var(--cor1)';

    if (colorMode === 'dark') {
        document.getElementById('dark-mode').style.display = 'none'
        document.getElementById('light-mode').style.display = 'block'

        document.getElementById('page').style.backgroundColor = COR1
        document.querySelector("p").style.color = COR0
        document.getElementById("message").style.color = COR0
        document.querySelector("h1").style.color = COR0
        document.querySelector("label").style.color = COR0
    } else {
        document.getElementById('dark-mode').style.display = 'block'
        document.getElementById('light-mode').style.display = 'none'

        document.getElementById('page').style.backgroundColor = COR0
        document.querySelector("p").style.color = COR1
        document.getElementById("message").style.color = COR1
        document.querySelector("h1").style.color = COR1
        document.querySelector("label").style.color = COR1
    }
}