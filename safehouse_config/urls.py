"""
URL v konfigurační složce safehouse_config project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('safehouse_app.urls')),
]
