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
         views.detail_pojistence, name="detail_pojistence"),
    path('klienti/pridat',
         views.pridat_pojistence, name="pridat_pojistence"),
    path('klienti/vymazat',
         views.vymazat_pojistence, name="vymazat_pojistence"),
    path('klienti/vymazat/<int:del_id>',
         views.vymazat_pojistence_id, name="vymazat_pojistence_id"),
    path('klienti/editovat/<int:edit_id>',
         views.editovat_pojistence, name="editovat_pojistence"),


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
