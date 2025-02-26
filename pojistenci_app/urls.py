# URLs v aplikaci

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
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
    path('pojisteni',
         views.pojisteni, name="pojisteni"),
    path('pojisteni/pridat',
         views.pridat_pojisteni, name="pridat_pojisteni"),
    path('pojisteni/editovat/<int:edit_id>',
         views.editovat_pojisteni, name="editovat_pojisteni"),
    path('pojisteni/vymazat/<int:del_produkt_id>',
         views.vymazat_pojisteni, name="vymazat_pojisteni"),

]
