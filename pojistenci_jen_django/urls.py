"""
URL v konfigurační složce pojistenci_jen_django project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pojistenci_app.urls')),
]
