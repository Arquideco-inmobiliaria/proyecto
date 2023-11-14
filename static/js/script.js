<<<<<<< HEAD
hamburges = document.querySelector(".hamburguesa");

=======
const nav=document.querySelector("#nav")
const menu=document.querySelector("#menu")
const boton=document.querySelector("#boton")
const bot=document.querySelector("#bot")
const logo=document.querySelector("#logo")


boton.addEventListener("click", ()=>{
    menu.style.display="block";
    bot.style.display="none";
    nav.style.left="-150px";
    logo.style.margin="20px";
    logo.style.marginTop="5px"


})
// boton.addEventListener("click", ()=>{
//     menu.style.display="none";
//     bot.style.display="block";
//     nav.style.left="-150px";
//     logo.style.margin="20px";
//     logo.style.marginTop="5px"
// } )
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
>>>>>>> 087ea55bc6e1c1f7bdf6f25c2230a0a6dcdb8836

hamburges.onclick= function(){
    navBar = document.querySelector(".nav-bar")
    navBar.classList.toggle("active")
    ventana = document.querySelector(".ventana")
    ventana.classList.toggle("active")
}



