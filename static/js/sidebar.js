const button = document.getElementById("menu-toggle");
const sidebar = document.querySelector(".sidebar");

button.addEventListener("click", () => {
    sidebar.classList.toggle("open");
});

