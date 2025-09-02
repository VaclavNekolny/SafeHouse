from django.contrib import admin
from . models import Klienti, Produkty, Smlouvy, Historie

# Register your models here
admin.site.register(Klienti)
admin.site.register(Produkty)
admin.site.register(Smlouvy)
admin.site.register(Historie)
