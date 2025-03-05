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


def pridat_produkt(request):
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
        return render(request, 'pojistenci_app/pridat_produkt.html', {'message': message, 'pridat': True})

    return render(request, 'pojistenci_app/pridat_produkt.html', {'pridat': True})


def editovat_produkt(request, edit_id):

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
        return render(request, 'pojistenci_app/editovat_produkt.html', {'message': message, 'editovat': True})

    produkt_k_editaci = Produkty.objects.get(id=edit_id)
    return render(request, 'pojistenci_app/editovat_produkt.html', {'editovat': True, 'produkt': produkt_k_editaci})


def vymazat_produkt(request, del_produkt_id):
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


def detail_pojistence(request, id_klienta):
    pojistenec = Pojistenci.objects.get(id=id_klienta)
    smlouvy_klienta = Smlouvy.objects.filter(pojistenec_id__id=id_klienta)
    celkem_mesicne = smlouvy_klienta.aggregate(Sum('cena'))
    return render(request, 'pojistenci_app/smlouvy_pojistence.html', {'pojistenec': pojistenec, 'smlouvy': smlouvy_klienta, 'celkem_mesicne': celkem_mesicne})


def pridat_pojistence(request):
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
        novy_pojistenec = Pojistenci(jmeno=jmeno, prijmeni=prijmeni,
                                     narozeni=narozeni, foto=foto, je_muz=je_muz)
        novy_pojistenec.save()

        # Záznam do historie
        id = novy_pojistenec.id
        pojistenec = jmeno + " " + prijmeni
        detail_akce = f"Přidání Pojištěnce {jmeno} {prijmeni}"
        historie = Historie(pojistenec_id=id, pojistenec=pojistenec,
                            akce='Vytvoření', detail_akce=detail_akce)
        historie.save()

        message = f"Pojištěnec {jmeno} {prijmeni} přidán do databáze"
        return render(request, 'pojistenci_app/pridat_pojistence.html', {'message': message, 'pridat': True})

    return render(request, 'pojistenci_app/pridat_pojistence.html', {'pridat': True})


def vymazat_pojistence(request):

    pojistenci = Pojistenci.objects.all()

    if request.method == "POST":
        id = request.POST["pojistenci"]
        pojistenec_ke_smazani = Pojistenci.objects.get(id=id)

        jmeno = pojistenec_ke_smazani.jmeno
        prijmeni = pojistenec_ke_smazani.prijmeni

        # Záznam do historie
        id = pojistenec_ke_smazani.id
        pojistenec = jmeno + " " + prijmeni
        detail_akce = f"Smazání Pojištěnce {jmeno} {prijmeni}"
        historie = Historie(pojistenec_id=id, pojistenec=pojistenec,
                            akce='Smazání', detail_akce=detail_akce)
        historie.save()

        pojistenec_ke_smazani.delete()

        message = f"Pojištěnec {jmeno} {prijmeni} byl smazán z databáze."
        return render(request, 'pojistenci_app/vymazat_pojistence.html', {'message': message, 'vymazat': True, 'pojistenci': pojistenci})

    return render(request, 'pojistenci_app/vymazat_pojistence.html', {'vymazat': True, 'pojistenci': pojistenci})


def vymazat_pojistence_id(request, del_id):
    pojistenec_ke_smazani = Pojistenci.objects.get(id=del_id)

    # Záznam do historie
    jmeno = pojistenec_ke_smazani.jmeno
    prijmeni = pojistenec_ke_smazani.prijmeni
    id = pojistenec_ke_smazani.id
    pojistenec = jmeno + " " + prijmeni
    detail_akce = f"Smazání Pojištěnce {jmeno} {prijmeni}"
    historie = Historie(pojistenec_id=id, pojistenec=pojistenec,
                        akce='Smazání', detail_akce=detail_akce)
    historie.save()

    pojistenec_ke_smazani.delete()
    return redirect('klienti')


def editovat_pojistence(request, edit_id):

    if request.method == "POST":
        id = request.POST["id"]
        pojistenec_k_editaci = Pojistenci.objects.get(id=id)
        jmeno = request.POST["jmeno"]
        prijmeni = request.POST["prijmeni"]
        narozeni = request.POST["datum_narozeni"]
        pohlavi = request.POST["pohlavi"]

        # Fotka se změní pouze při změně pohlaví při editaci
        if (not pojistenec_k_editaci.je_muz and pohlavi == "muz") or (pojistenec_k_editaci.je_muz and pohlavi == "zena"):
            if pohlavi == "muz":
                foto = str(random.randint(1, 15))+".png"
                je_muz = True
            else:
                foto = str(random.randint(50, 65))+".png"
                je_muz = False
            pojistenec_k_editaci.foto = foto
            pojistenec_k_editaci.je_muz = je_muz

        pojistenec_k_editaci.jmeno = jmeno
        pojistenec_k_editaci.prijmeni = prijmeni
        pojistenec_k_editaci.narozeni = narozeni
        pojistenec_k_editaci.save()

        # Záznam do historie
        id = pojistenec_k_editaci.id
        pojistenec = jmeno + " " + prijmeni
        detail_akce = f"Editace pojištěnce {jmeno} {prijmeni}"
        historie = Historie(pojistenec_id=id, pojistenec=pojistenec,
                            akce='Editace', detail_akce=detail_akce)
        historie.save()

        message = f"Pojištěnec {jmeno} {prijmeni} editován"
        return render(request, 'pojistenci_app/editovat_pojistence.html', {'message': message, 'editovat': True})

    pojistenec_k_editaci = Pojistenci.objects.get(id=edit_id)
    return render(request, 'pojistenci_app/editovat_pojistence.html', {'editovat': True, 'pojistenec': pojistenec_k_editaci})


def nova_smlouva(request, klient_id):
    pojistenec = Pojistenci.objects.get(id=klient_id)
    if request.method == "POST":
        id_produktu = request.POST["produkty_id"]
        produkt = Produkty.objects.get(id=id_produktu)
        return render(request, 'pojistenci_app/vybrany_produkt.html', {'produkt': produkt, 'pojistenec': pojistenec})
    produkty = Produkty.objects.all()
    return render(request, 'pojistenci_app/nova_smlouva.html', {'produkty': produkty,
                                                                'pojistenec': pojistenec})


def podepsat(request, klient_id):

    produkt_id = request.POST["produkt_id"]
    pojistenec_id = request.POST["pojistenec_id"]
    castka_kryti = request.POST["castka_kryti"]

    produkt = Produkty.objects.get(id=produkt_id)

    cena_pojisteni = round(int(castka_kryti) / produkt.pomer)

    pojistenec = Pojistenci.objects.get(id=pojistenec_id)

    nova_smlouva = Smlouvy(pojistenec_id=pojistenec, produkt_id=produkt,
                           castka_kryti=castka_kryti, cena=cena_pojisteni)
    nova_smlouva.save()

    # Záznam do historie
    pojistenec_id = pojistenec.id
    produkt_id = produkt.id
    smlouva_id = nova_smlouva.id
    pojistenec = pojistenec.prijmeni + " " + pojistenec.jmeno
    produkt = produkt.nazev
    detail_akce = f"{pojistenec} podepsal smlouvu {produkt}"
    historie = Historie(pojistenec_id=pojistenec_id, produkt_id=produkt_id,
                        smlouva_id=smlouva_id, pojistenec=pojistenec, produkt=produkt,
                        akce='Podpis', detail_akce=detail_akce)
    historie.save()

    return redirect('detail_pojistence', klient_id)


def vymazat_smlouvu(request, klient_id, delete_id):
    smlouva_k_vymazani = Smlouvy.objects.get(id=delete_id)

    # Záznam do historie
    pojistenec_id = smlouva_k_vymazani.pojistenec_id.id
    produkt_id = smlouva_k_vymazani.produkt_id.id
    smlouva_id = smlouva_k_vymazani.id
    pojistenec = smlouva_k_vymazani.pojistenec_id.prijmeni + \
        " " + smlouva_k_vymazani.pojistenec_id.jmeno
    produkt = smlouva_k_vymazani.produkt_id.nazev
    detail_akce = f"{pojistenec} vypověděl smlouvu {produkt}"
    historie = Historie(pojistenec_id=pojistenec_id, produkt_id=produkt_id,
                        smlouva_id=smlouva_id, pojistenec=pojistenec, produkt=produkt,
                        akce='Výpověď', detail_akce=detail_akce)
    historie.save()

    smlouva_k_vymazani.delete()

    return redirect(reverse('detail_pojistence', kwargs={'id_klienta': klient_id}))


def smlouvy(request):
    sort_param = request.GET.get("sort", "id")

    smlouvy = Smlouvy.objects.all().order_by(sort_param)
    inkaso_celkem = smlouvy.aggregate(Sum('cena'))
    return render(request, 'pojistenci_app/smlouvy.html', {'smlouvy': smlouvy,
                                                           'inkaso_celkem': inkaso_celkem,
                                                           'sort_param': sort_param})


def historie(request):
    historie = Historie.objects.all().order_by('-datum_cas')
    return render(request, 'pojistenci_app/historie.html', {'historie': historie})
