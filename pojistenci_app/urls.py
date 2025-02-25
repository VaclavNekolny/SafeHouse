# URLs v aplikaci

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('klienti', views.klienti, name="klienti"),
    path('klienti/pridat',
         views.pridat_pojistence, name="pridat_pojistence"),
    path('klienti/vymazat',
         views.vymazat_pojistence, name="vymazat_pojistence"),
    path('klienti/vymazat/<int:del_id>',
         views.vymazat_pojistence_id, name="vymazat_pojistence_id"),
    path('klienti/<int:edit_id>',
         views.editovat_pojistence, name="editovat_pojistence")

]
