from django.db import models


# Create your models here.

class Klienti(models.Model):
    jmeno = models.CharField(max_length=40, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=40, verbose_name="Příjmení")
    je_muz = models.BooleanField(default=True)
    narozeni = models.DateField(verbose_name="Datum narození")
    foto = models.CharField(
        max_length=60, verbose_name="Název obrázku")
    datum_registrace = models.DateField(auto_now=True)

    def __str__(self):
        return f"Klient: {self.jmeno} {self.prijmeni}, Narozen: {self.narozeni}, Foto: {self.foto}, Registrován: {self.datum_registrace}"

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienti"


class Produkty(models.Model):
    nazev = models.CharField(max_length=80, verbose_name="Název produktu")
    predmet_kryti = models.CharField(
        max_length=200, verbose_name="Předmět krytí")
    zakladni_castka = models.IntegerField(
        verbose_name="Základní částka krytí")
    zakladni_cena = models.IntegerField(verbose_name="Základní cena")
    pomer = models.FloatField("Poměr mezi částkou krytí a cenou pojištění")

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def __str__(self):
        return f"Název produktu: {self.nazev}, Krytí: {self.predmet_kryti}, Částka: {self.zakladni_castka}kč, Cena: {self.zakladni_cena}kč"


class Smlouvy(models.Model):
    klient = models.ForeignKey(Klienti, on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkty, on_delete=models.CASCADE)
    castka_kryti = models.IntegerField(verbose_name="Částka krytí")
    cena = models.FloatField(verbose_name="Cena")
    datum = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Smlouvy"


class Historie(models.Model):
    klient_id = models.IntegerField(null=True)
    produkt_id = models.IntegerField(null=True)
    smlouva_id = models.IntegerField(null=True)
    klient_str = models.CharField(max_length=40, null=True)
    produkt_str = models.CharField(max_length=40, null=True)
    akce = models.CharField(max_length=10, null=True)
    detail_akce = models.CharField(max_length=200, null=True)
    datum_cas = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Akce: {self.akce}, {self.detail_akce}"

    class Meta:
        verbose_name_plural = "Historie událostí"
