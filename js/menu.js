

let menu = document.getElementById("menu")
let header = document.getElementById("header")
let nav = document.getElementById("nav")

menu.addEventListener("click", function() {
if(header.style.height == "85px" || header.offsetHeight == 80) {
    header.style.height = 85 + nav.offsetHeight + "px"
} else {
    header.style.height = "85px"
}
    

})