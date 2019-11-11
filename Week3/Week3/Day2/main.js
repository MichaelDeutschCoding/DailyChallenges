let butt = document.getElementById("butt");
let body = document.getElementsByTagName("body")[0];

setTimeout(function() {
    butt.classList.add("clowns")
}, 900);

butt.addEventListener("mouseover", function() {
    this.style.height = "250px";
    this.style.border = "5px solid yellow";
})

butt.addEventListener("mouseleave", function(){
    this.style.height = "150px";
    this.style.border = "none";

})

window.addEventListener("mousedown", function() {
    butt.style.left = "200px";
    butt.style.top = "180px";
})

butt.addEventListener("click", function() {
    butt.classList.add("fire");
    butt.innerHTML = "Watch Out!!";
    setTimeout(function() {
        butt.classList.remove("fire");
        butt.innerHTML = "You got burned!"
    }, 500)
})

butt.addEventListener("drag", function(event){
    body.style.background = "yellow";
    this.className = "moving";
    this.innerHTML = "AAAAAHHHH!!!!";
    this.style.top = event.clientY + "px";
    this.style.left = event.clientX + "px";
})

butt.addEventListener("dragend", function() {
    body.style.background = "url(space.jpg)";
    butt.className = "clowns";
    this.style.top = event.clientY + "px";
    this.style.left = event.clientX + "px";
    this.innerHTML = "Click Here to See WILD Things Happen!"

})

window.addEventListener("keydown", reset);

function reset(){
    butt.className = "pink";
    butt.innerHTML = "WHAT's HAPPENNING?!?";
    butt.style.transform = "rotate(45deg)";


    setTimeout( function() {
        butt.style.transform = "rotate(0deg)";
        butt.className = "clowns"
        butt.style.left = "400px";
        butt.style.top = "350px";
        butt.innerHTML = "Ok, Let's Get Wild. Click Here for Craziness!!"
    }, 600);
}

window.addEventListener("scroll", function() {
    butt.style.transform = "scale(2, 2)";
    setTimeout(function(){
        butt.style.transform = "scale(1, 1)"
    }, 600)
})