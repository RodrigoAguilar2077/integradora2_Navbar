function toggleMenu() {
    var navbar = document.getElementById("navbar");
    if (navbar.classList.contains("show")) {
        navbar.classList.remove("show");
    } else {
        navbar.classList.add("show");
    }
}
