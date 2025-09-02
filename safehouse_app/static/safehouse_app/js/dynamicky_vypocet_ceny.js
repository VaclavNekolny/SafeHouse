function dynamickyVypocet() {
  let castka = document.getElementById("castka").value;
  let pomer = document.getElementById("pomer").value;
  let cena = document.getElementById("cena");

  if (castka !== "") {
    let vysledek = parseFloat(castka) / parseFloat(pomer);
    cena.innerText = "Cena/měs.: " + vysledek.toFixed(2) + "kč";
  } else {
    cena.innerText = "";
  }
}

document.getElementById("castka").addEventListener("input", dynamickyVypocet);

document.addEventListener("DOMContentLoaded", dynamickyVypocet);
