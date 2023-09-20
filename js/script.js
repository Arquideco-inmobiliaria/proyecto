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





