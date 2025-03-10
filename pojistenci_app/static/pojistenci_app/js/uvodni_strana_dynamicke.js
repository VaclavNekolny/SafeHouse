let lastOpened = null; // Uchovává poslední otevřený obsah

function changeContent(option) {
  const content = document.getElementById("dynamicContent");
  const imageWrapper = document.getElementById("about_foto_wrapper");
  const heroDiv = document.getElementById("heroDiv");
  const collapseElement = new bootstrap.Collapse(
    document.getElementById("collapseContent"),
    {
      toggle: false,
    }
  );
  const collapseDiv = document.getElementById("collapseContent");

  // Pokud klikneš na stejné tlačítko a collaps je už otevřený, zavři ho
  if (lastOpened === option && collapseDiv.classList.contains("show")) {
    collapseElement.hide();
    lastOpened = null;
    return;
  }

  let o_aplikaci = `Aplikace SafeHouse vznikla jako závěrečný projekt v rekvalifikačním kurzu ITnetwork. 
    Následně jsem se ji pokusil vyladit po stránce grafické i funkční tak, jak to zatím umím nejlépe. 
    <b class='d-block mt-2'>Použité technologie:</b><br>
    Django, Python, HTML, CSS, Bootstrap, JavaScript`;

  let funkce_aplikace = `<p>CRUD správa klientů, pojišťovacích produktů a podepsaných smluv konkrétních klientů.</p>
            <p>Do testovací vezre aplikace se může přihlásit každý z pozice administrátora i s pozice klienta. 
                Aplikace se po 20 minutách neaktivity automaticky restartuje do defaultní podoby,
                    aby se předešlo zbytečnému naplnění databáze.</p>`;

  let o_tvurci = `
                    <div class="row">
                        <div class="col-6 offset-3">
                            <p>Jmenuji se <strong>Václav Nekolný</strong> a jsem začínající programátor.
                            Baví mě se stále učit nové věci, zkoumat věci do hloubky a přicházet jim na kloub.<br>
                            Mám rád, když věci hezky vypadají, efektivně fungují a jsou logicky vystavěné.<br>
                            Miluji klávesové zkratky!
                            </p>
                            <svg width="25" height="25" fill="#777777" class="bi bi-linkedin" viewBox="0 0 16 16">
                                <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854zm4.943 12.248V6.169H2.542v7.225zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248S2.4 3.226 2.4 3.934c0 .694.521 1.248 1.327 1.248zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016l.016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225z"/>
                            </svg>
                            LinkedIn
                        </div>
                    </div>`;

  // Změna obsahu podle tlačítka
  if (option === 1) {
    content.innerHTML = o_aplikaci;
    imageWrapper.style.display = "none";
    heroDiv.style.filter = "none";
  } else if (option === 2) {
    content.innerHTML = funkce_aplikace;
    imageWrapper.style.display = "none";
    heroDiv.style.filter = "none";
  } else if (option === 3) {
    content.innerHTML = o_tvurci;

    if (!collapseDiv.classList.contains("show")) {
      imageWrapper.style.display = "none";
      heroDiv.style.filter = "none";
    } else {
      imageWrapper.style.display = "block";
      heroDiv.style.filter = "blur(5px)";
    }
  }

  // Uložení posledního tlačítka
  lastOpened = option;

  // Pokud není collaps otevřený, otevřeme ho
  if (!collapseDiv.classList.contains("show")) {
    collapseElement.show();
  }
}
