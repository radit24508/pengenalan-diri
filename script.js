// script.js
document.getElementById("tahun").textContent = new Date().getFullYear();

const tombol = document.getElementById("tombolSalam");
const pesan = document.getElementById("pesan");

tombol.addEventListener("click", () => {
  pesan.textContent = "Hai juga! Senang bisa kenalan sama kamu 😊";
  pesan.style.color = "#38bdf8";
});
