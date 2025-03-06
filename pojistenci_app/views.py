from django.shortcuts import render, redirect
from django.urls import reverse
from pojistenci_app.models import Pojistenci, Produkty, Smlouvy, Historie
from django.db.models import Sum
import random


def index(request):
    pojistenci = Pojistenci.objects.all()
    return render(request, "pojistenci_app/index.html", {'pojistenci': pojistenci})


def produkty(request):
    pojistovaci_produkty = Produkty.objects.all()
    return render(request, 'pojistenci_app/produkty.html', {'produkty': pojistovaci_produkty})


def produkt_pridat(request):
    if request.method == "POST":
        nazev = request.POST["nazev"]
        predmet_kryti = request.POST["predmet_kryti"]
        castka = request.POST["castka"]
        cena = request.POST["cena"]
        pomer = round(int(castka)/int(cena), 2)

        novy_produkt = Produkty(nazev=nazev, predmet_kryti=predmet_kryti,
                                zakladni_castka=castka, zakladni_cena=cena, pomer=pomer)
        novy_produkt.save()

        # Záznam do historie
        id = novy_produkt.id
        produkt = novy_produkt.nazev
        detail_akce = f"Přidání produktu {produkt}"
        historie = Historie(produkt_id=id, produkt=produkt,
                            akce='Vytvoření', detail_akce=detail_akce)
        historie.save()

        message = f"Produkt '{nazev}' přidán do databáze"
        return render(request, 'pojistenci_app/produkt_pridat.html', {'message': message, 'pridat': True})

    return render(request, 'pojistenci_app/produkt_pridat.html', {'pridat': True})


def produkt_editovat(request, edit_id):

    if request.method == "POST":
        id = request.POST["id"]
        produkt_k_editaci = Produkty.objects.get(id=id)
        nazev = request.POST["nazev"]
        predmet_kryti = request.POST["predmet_kryti"]
        castka = request.POST["castka"]
        cena = request.POST["cena"]
        pomer = round(int(castka)/int(cena), 2)

        produkt_k_editaci.nazev = nazev
        produkt_k_editaci.predmet_kryti = predmet_kryti
        produkt_k_editaci.zakladni_castka = castka
        produkt_k_editaci.zakladni_cena = cena
        produkt_k_editaci.pomer = pomer
        produkt_k_editaci.save()

        # Záznam do historie
        id = produkt_k_editaci.id
        produkt = produkt_k_editaci.nazev
        detail_akce = f"Editace pojištění {produkt}"
        historie = Historie(produkt_id=id, produkt=produkt,
                            akce='Editace', detail_akce=detail_akce)
        historie.save()

        message = f"Produkt '{nazev}' editován"
        return render(request, 'pojistenci_app/produkt_editovat.html', {'message': message, 'editovat': True})

    produkt_k_editaci = Produkty.objects.get(id=edit_id)
    return render(request, 'pojistenci_app/produkt_editovat.html', {'editovat': True, 'produkt': produkt_k_editaci})


def produkt_vymazat(request, del_produkt_id):
    produkt_k_vymazani = Produkty.objects.get(id=del_produkt_id)

    # Záznam do historie
    id = produkt_k_vymazani.id
    produkt = produkt_k_vymazani.nazev
    detail_akce = f"Vymazání produktu '{produkt}'"
    historie = Historie(produkt_id=id, produkt=produkt,
                        akce='Smazání', detail_akce=detail_akce)
    historie.save()

    produkt_k_vymazani.delete()
    return redirect('produkty')


def klienti(request):
    vsichni_klienti = Pojistenci.objects.all()
    return render(request, 'pojistenci_app/klienti.html', {'klienti': vsichni_klienti})


def klient_detail(request, id_klienta):
    klient = Pojistenci.objects.get(id=id_klienta)
    smlouvy_klienta = Smlouvy.objects.filter(pojistenec_id__id=id_klienta)
    celkem_mesicne = smlouvy_klienta.aggregate(Sum('cena'))
    return render(request, 'pojistenci_app/klient_smlouvy.html', {'klient': klient, 'smlouvy': smlouvy_klienta, 'celkem_mesicne': celkem_mesicne})


def klient_pridat(request):
    if request.method == "POST":
        jmeno = request.POST["jmeno"]
        prijmeni = request.POST["prijmeni"]
        narozeni = request.POST["datum_narozeni"]
        pohlavi = request.POST["pohlavi"]

        if pohlavi == "muz":
            foto = str(random.randint(1, 15))+".png"
            je_muz = True
        else:
            foto = str(random.randint(50, 65))+".png"
            je_muz = False

        # Uložení do databáze
        novy_klient = Pojistenci(jmeno=jmeno, prijmeni=prijmeni,
                                 narozeni=narozeni, foto=foto, je_muz=je_muz)
        novy_klient.save()

        # Záznam do historie
        id = novy_klient.id
        klient = jmeno + " " + prijmeni
        detail_akce = f"Přidání klienta {jmeno} {prijmeni}"
        historie = Historie(pojistenec_id=id, pojistenec=klient,
                            akce='Vytvoření', detail_akce=detail_akce)
        historie.save()

        message = f"Klient {jmeno} {prijmeni} přidán do databáze"
        return render(request, 'pojistenci_app/klient_pridat.html', {'message': message, 'pridat': True})

    return render(request, 'pojistenci_app/klient_pridat.html', {'pridat': True})


def klient_vymazat(request):

    klienti = Pojistenci.objects.all()

    if request.method == "POST":
        id = request.POST["klient_id"]
        klient_ke_smazani = Pojistenci.objects.get(id=id)

        jmeno = klient_ke_smazani.jmeno
        prijmeni = klient_ke_smazani.prijmeni

        # Záznam do historie
        id = klient_ke_smazani.id
        klient = jmeno + " " + prijmeni
        detail_akce = f"Smazání klienta {jmeno} {prijmeni}"
        historie = Historie(pojistenec_id=id, pojistenec=klient,
                            akce='Smazání', detail_akce=detail_akce)
        historie.save()

        klient_ke_smazani.delete()

        message = f"Klient {jmeno} {prijmeni} byl smazán z databáze."
        return render(request, 'pojistenci_app/klient_vymazat.html', {'message': message, 'vymazat': True, 'klienti': klienti})

    return render(request, 'pojistenci_app/klient_vymazat.html', {'vymazat': True, 'klienti': klienti})


def klient_vymazat_podle_id(request, klient_id):
    klient_ke_smazani = Pojistenci.objects.get(id=klient_id)

    # Záznam do historie
    jmeno = klient_ke_smazani.jmeno
    prijmeni = klient_ke_smazani.prijmeni
    id = klient_ke_smazani.id
    klient = jmeno + " " + prijmeni
    detail_akce = f"Smazání klienta {jmeno} {prijmeni}"
    historie = Historie(pojistenec_id=id, pojistenec=klient,
                        akce='Smazání', detail_akce=detail_akce)
    historie.save()

    klient_ke_smazani.delete()
    return redirect('klienti')


def klient_editovat(request, klient_id):

    if request.method == "POST":
        id = request.POST["id"]
        klient_k_editaci = Pojistenci.objects.get(id=id)
        jmeno = request.POST["jmeno"]
        prijmeni = request.POST["prijmeni"]
        narozeni = request.POST["datum_narozeni"]
        pohlavi = request.POST["pohlavi"]

        # Fotka se změní pouze při změně pohlaví při editaci
        if (not klient_k_editaci.je_muz and pohlavi == "muz") or (klient_k_editaci.je_muz and pohlavi == "zena"):
            if pohlavi == "muz":
                foto = str(random.randint(1, 15))+".png"
                je_muz = True
            else:
                foto = str(random.randint(50, 65))+".png"
                je_muz = False
            klient_k_editaci.foto = foto
            klient_k_editaci.je_muz = je_muz

        klient_k_editaci.jmeno = jmeno
        klient_k_editaci.prijmeni = prijmeni
        klient_k_editaci.narozeni = narozeni
        klient_k_editaci.save()

        # Záznam do historie
        id = klient_k_editaci.id
        klient = jmeno + " " + prijmeni
        detail_akce = f"Editace klienta {jmeno} {prijmeni}"
        historie = Historie(pojistenec_id=id, pojistenec=klient,
                            akce='Editace', detail_akce=detail_akce)
        historie.save()

        message = f"Klient {jmeno} {prijmeni} editován"
        return render(request, 'pojistenci_app/klient_editovat.html', {'message': message, 'editovat': True})

    klient_k_editaci = Pojistenci.objects.get(id=klient_id)
    return render(request, 'pojistenci_app/klient_editovat.html', {'editovat': True, 'klient': klient_k_editaci})


# SMLOUVY (klient-produkt)

def smlouvy(request):
    sort_param = request.GET.get("sort", "id")

    smlouvy = Smlouvy.objects.all().order_by(sort_param)
    inkaso_celkem = smlouvy.aggregate(Sum('cena'))
    return render(request, 'pojistenci_app/smlouvy.html', {'smlouvy': smlouvy,
                                                           'inkaso_celkem': inkaso_celkem,
                                                           'sort_param': sort_param})


def smlouva_nova(request, klient_id):
    klient = Pojistenci.objects.get(id=klient_id)
    if request.method == "POST":
        id_produktu = request.POST["produkty_id"]
        produkt = Produkty.objects.get(id=id_produktu)
        return render(request, 'pojistenci_app/produkt_vybrany.html', {'produkt': produkt, 'klient': klient})
    produkty = Produkty.objects.all()
    return render(request, 'pojistenci_app/smlouva_nova.html', {'produkty': produkty,
                                                                'klient': klient})


def smlouva_podepsat(request, klient_id):
    produkt_id = request.POST["produkt_id"]
    castka_kryti = request.POST["castka_kryti"]
    produkt = Produkty.objects.get(id=produkt_id)

    # Vypočítá cenu pojištění z čáskty krytí a poměru, který se uložil do databáze při vytváření projektu
    cena_pojisteni = round(int(castka_kryti) / produkt.pomer)
    klient = Pojistenci.objects.get(id=klient_id)

    nova_smlouva = Smlouvy(pojistenec_id=klient, produkt_id=produkt,
                           castka_kryti=castka_kryti, cena=cena_pojisteni)
    nova_smlouva.save()

    # Záznam do historie
    produkt_id = produkt.id
    smlouva_id = nova_smlouva.id
    klient_str = klient.prijmeni + " " + klient.jmeno
    produkt = produkt.nazev
    detail_akce = f"{klient_str} podepsal smlouvu {produkt}"
    historie = Historie(pojistenec_id=klient_id, produkt_id=produkt_id,
                        smlouva_id=smlouva_id, pojistenec=klient_str, produkt=produkt,
                        akce='Podpis', detail_akce=detail_akce)
    historie.save()

    return redirect('klient_detail', klient_id)


def smlouva_vymazat(request, klient_id, smlouva_id):
    smlouva_k_vymazani = Smlouvy.objects.get(id=smlouva_id)

    # Záznam do historie
    produkt_id = smlouva_k_vymazani.produkt_id.id
    smlouva_id = smlouva_k_vymazani.id
    klient_str = smlouva_k_vymazani.pojistenec_id.prijmeni + \
        " " + smlouva_k_vymazani.pojistenec_id.jmeno
    produkt = smlouva_k_vymazani.produkt_id.nazev
    detail_akce = f"{klient_str} vypověděl smlouvu {produkt}"
    historie = Historie(pojistenec_id=klient_id, produkt_id=produkt_id,
                        smlouva_id=smlouva_id, pojistenec=klient_str, produkt=produkt,
                        akce='Výpověď', detail_akce=detail_akce)
    historie.save()

    smlouva_k_vymazani.delete()

    return redirect(reverse('klient_detail', kwargs={'id_klienta': klient_id}))


def historie(request):
    historie = Historie.objects.all().order_by('-datum_cas')
    return render(request, 'pojistenci_app/historie.html', {'historie': historie})
