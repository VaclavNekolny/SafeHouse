# URLs v aplikaci

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    # POJIŠTĚNÍ
    path('produkty',
         views.produkty, name="produkty"),
    path('produkty/pridat',
         views.pridat_produkt, name="pridat_produkt"),
    path('produkty/editovat/<int:edit_id>',
         views.editovat_produkt, name="editovat_produkt"),
    path('produkty/vymazat/<int:del_produkt_id>',
         views.vymazat_produkt, name="vymazat_produkt"),

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
         views.nova_smlouva, name="nova_smlouva"),
    path('klienti/<int:klient_id>/podepsat',
         views.podepsat, name="podepsat"),
    path('klienti/<int:klient_id>/vymazat/<int:delete_id>',
         views.vymazat_smlouvu, name="vymazat_smlouvu"),


    # SMLOUVY
    path('smlouvy',
         views.smlouvy, name="smlouvy"),


    # HISTORIE
    path('historie',
         views.historie, name="historie"),
]
