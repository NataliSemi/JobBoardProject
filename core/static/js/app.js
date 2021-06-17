// // mobile menu
// const burgerIcon = document.querySelector('#burger');
// const navbarMenu = document.querySelector('#nav-links');

// burgerIcon.addEventListener('click', () => {
//     navbarMenu.classList.toggle('is-active')
// })

const navToggle = document.querySelector("#burger");
const links = document.querySelector("#navMenu");

navToggle.addEventListener('click', function(){
    links.classList.toggle("is-active");
});