from django.shortcuts import render, redirect
from django.http import HttpResponse
from pojistenci_app.models import Pojistenci
import random

# Create your views here.


def index(request):
    pojistenci = Pojistenci.objects.all()
    return render(request, "pojistenci_app/index.html", {'pojistenci': pojistenci})


def klienti(request):
    vsichni_klienti = Pojistenci.objects.all()
    return render(request, 'pojistenci_app/klienti.html', {'klienti': vsichni_klienti})


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
