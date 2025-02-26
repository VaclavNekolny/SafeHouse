from django.shortcuts import render, redirect
from django.urls import reverse
from pojistenci_app.models import Pojistenci, Produkty, Smlouvy
import random

# Create your views here.


def index(request):
    pojistenci = Pojistenci.objects.all()
    return render(request, "pojistenci_app/index.html", {'pojistenci': pojistenci})


def klienti(request):
    vsichni_klienti = Pojistenci.objects.all()
    return render(request, 'pojistenci_app/klienti.html', {'klienti': vsichni_klienti})


def detail_pojistence(request, id_klienta):
    pojistenec = Pojistenci.objects.get(id=id_klienta)
    smlouvy_klienta = Smlouvy.objects.filter(pojistenec_id__id=id_klienta)
    return render(request, 'pojistenci_app/smlouvy_pojistence.html', {'pojistenec': pojistenec, 'smlouvy': smlouvy_klienta})


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

        novy_pojistenec = Pojistenci(jmeno=jmeno, prijmeni=prijmeni,
                                     narozeni=narozeni, foto=foto, je_muz=je_muz)
        novy_pojistenec.save()

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
        pojistenec_ke_smazani.delete()

        message = f"Pojištěnec {jmeno} {prijmeni} byl smazán z databáze."
        return render(request, 'pojistenci_app/vymazat_pojistence.html', {'message': message, 'vymazat': True, 'pojistenci': pojistenci})

    return render(request, 'pojistenci_app/vymazat_pojistence.html', {'vymazat': True, 'pojistenci': pojistenci})


def vymazat_pojistence_id(request, del_id):
    pojistenec_k_vymazani = Pojistenci.objects.get(id=del_id)
    pojistenec_k_vymazani.delete()
    return redirect('klienti')


def editovat_pojistence(request, edit_id):

    if request.method == "POST":
        id = request.POST["id"]
        pojistenec_k_editaci = Pojistenci.objects.get(id=id)
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

        pojistenec_k_editaci.jmeno = jmeno
        pojistenec_k_editaci.prijmeni = prijmeni
        pojistenec_k_editaci.narozeni = narozeni
        pojistenec_k_editaci.foto = foto
        pojistenec_k_editaci.je_muz = je_muz
        pojistenec_k_editaci.save()

        message = f"Pojištěnec {jmeno} {prijmeni} editován"
        return render(request, 'pojistenci_app/editovat_pojistence.html', {'message': message, 'editovat': True})

    pojistenec_k_editaci = Pojistenci.objects.get(id=edit_id)
    return render(request, 'pojistenci_app/editovat_pojistence.html', {'editovat': True, 'pojistenec': pojistenec_k_editaci})


def pojisteni(request):
    pojistovaci_produkty = Produkty.objects.all()
    return render(request, 'pojistenci_app/pojisteni.html', {'produkty': pojistovaci_produkty})


def pridat_pojisteni(request):
    if request.method == "POST":
        nazev = request.POST["nazev"]
        predmet_kryti = request.POST["predmet_kryti"]
        castka = request.POST["castka"]
        cena = request.POST["cena"]
        pomer = round(int(castka)/int(cena), 2)

        nove_pojisteni = Produkty(nazev=nazev, predmet_kryti=predmet_kryti,
                                  zakladni_castka=castka, zakladni_cena=cena, pomer=pomer)
        nove_pojisteni.save()

        message = f"Pojištění {nazev} přidáno do databáze"
        return render(request, 'pojistenci_app/pridat_pojisteni.html', {'message': message, 'pridat': True})

    return render(request, 'pojistenci_app/pridat_pojisteni.html', {'pridat': True})


def editovat_pojisteni(request, edit_id):

    if request.method == "POST":
        id = request.POST["id"]
        pojisteni_k_editaci = Produkty.objects.get(id=id)
        nazev = request.POST["nazev"]
        predmet_kryti = request.POST["predmet_kryti"]
        castka = request.POST["castka"]
        cena = request.POST["cena"]
        pomer = round(int(castka)/int(cena), 2)

        pojisteni_k_editaci.nazev = nazev
        pojisteni_k_editaci.predmet_kryti = predmet_kryti
        pojisteni_k_editaci.zakladni_castka = castka
        pojisteni_k_editaci.zakladni_cena = cena
        pojisteni_k_editaci.pomer = pomer
        pojisteni_k_editaci.save()

        message = f"Pojištění '{nazev}' editováno"
        return render(request, 'pojistenci_app/editovat_pojisteni.html', {'message': message, 'editovat': True})

    pojisteni_k_editaci = Produkty.objects.get(id=edit_id)
    return render(request, 'pojistenci_app/editovat_pojisteni.html', {'editovat': True, 'pojisteni': pojisteni_k_editaci})


def vymazat_pojisteni(request, del_produkt_id):
    pojisteni_k_vymazani = Produkty.objects.filter(id=del_produkt_id)
    pojisteni_k_vymazani.delete()
    return redirect('pojisteni')


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

    return redirect('detail_pojistence', klient_id)


def vymazat_smlouvu(request, klient_id, delete_id):
    smlouva_k_vymazani = Smlouvy.objects.get(id=delete_id)
    smlouva_k_vymazani.delete()

    return redirect(reverse('detail_pojistence', kwargs={'id_klienta': klient_id}))
