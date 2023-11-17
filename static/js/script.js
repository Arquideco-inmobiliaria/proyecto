hamburges = document.querySelector(".hamburguesa");

function agregarInputFile() {
    const inputFile = document.querySelector('.imagenes');
    const clone = inputFile.cloneNode(true);
    

    // Limpiar el valor del nuevo campo de entrada
    clone.value = '';

    const addButton = document.querySelector('button');
    addButton.parentNode.insertBefore(clone , addButton);
    const lineBreak = document.createElement('br');
    addButton.parentNode.insertBefore(lineBreak, addButton);
}

hamburges.onclick= function(){
    navBar = document.querySelector(".nav-bar")
    navBar.classList.toggle("active")
    ventana = document.querySelector(".ventana")
    ventana.classList.toggle("active")
}



