from django.contrib import admin
from . models import Pojistenci, Produkty, Smlouvy, SmluvniUdalosti

# Register your models here
admin.site.register(Pojistenci)
admin.site.register(Produkty)
admin.site.register(Smlouvy)
admin.site.register(SmluvniUdalosti)
