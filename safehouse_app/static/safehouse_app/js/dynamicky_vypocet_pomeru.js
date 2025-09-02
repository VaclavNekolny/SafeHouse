function dynamickyVypocet() {
  let castka = document.getElementById("castka").value;
  let cena = document.getElementById("cena").value;
  let pomer = document.getElementById("pomer");

  if (castka !== "" && cena !== "") {
    let vysledek = parseFloat(castka) / parseFloat(cena);
    pomer.innerText = "Poměr: " + vysledek.toFixed(2);
  } else {
    pomer.innerText = "";
  }
}

document.getElementById("castka").addEventListener("input", dynamickyVypocet);
document.getElementById("cena").addEventListener("input", dynamickyVypocet);

document.addEventListener("DOMContentLoaded", dynamickyVypocet);
