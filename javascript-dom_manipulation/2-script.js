var red_header = document.getElementById("red_header");
var header = document.querySelector("header")
red_header.addEventListener("click", add_class_red);

function add_class_red(){
    header.classList.add("red");
}