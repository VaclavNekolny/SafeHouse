# URLs v aplikaci

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    # POJIŠTĚNÍ
    path('produkty',
         views.produkty, name="produkty"),
    path('produkty/pridat',
         views.produkt_pridat, name="produkt_pridat"),
    path('produkty/editovat/<int:edit_id>',
         views.produkt_editovat, name="produkt_editovat"),
    path('produkty/vymazat/<int:del_produkt_id>',
         views.produkt_vymazat, name="produkt_vymazat"),

    # KLIENTI
    path('klienti', views.klienti, name="klienti"),
    path('klienti/<int:id_klienta>/',
         views.klient_detail, name="klient_detail"),
    path('klienti/pridat',
         views.klient_pridat, name="klient_pridat"),
    path('klienti/vymazat',
         views.klient_vymazat, name="klient_vymazat"),
    path('klienti/vymazat/<int:klient_id>',
         views.klient_vymazat_podle_id, name="klient_vymazat_podle_id"),
    path('klienti/editovat/<int:klient_id>',
         views.klient_editovat, name="klient_editovat"),


    # KLIENTI-SMLOUVY
    path('klienti/<int:klient_id>/nova_smlouva',
         views.smlouva_nova, name="smlouva_nova"),
    path('klienti/<int:klient_id>/podepsat',
         views.smlouva_podepsat, name="smlouva_podepsat"),
    path('klienti/<int:klient_id>/vymazat/<int:smlouva_id>',
         views.smlouva_vymazat, name="smlouva_vymazat"),


    # SMLOUVY
    path('smlouvy',
         views.smlouvy, name="smlouvy"),


    # HISTORIE
    path('historie',
         views.historie, name="historie"),
 

    # NEDOSTUPNÉ
    path('nedostupne',
         views.nedostupne, name="nedostupne"),

]
