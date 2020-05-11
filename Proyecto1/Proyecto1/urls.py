"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Proyecto1.views import saludo, despedida, darFecha, calculaEdad, saludo_plantilla, saludo_plantilla2, saludo_plantilla3, saludo_plantilla4, curso, cursoDjango

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('nosveremos/', despedida),
    path('fecha/', darFecha),
    path('edades/<int:edad>/<int:agno>', calculaEdad),
    path('saludoPlantilla/', saludo_plantilla),
    path('saludoPlantilla2', saludo_plantilla2),
    path('saludoPlantilla3', saludo_plantilla3),
    path('saludoPlantilla4', saludo_plantilla4),
    path('curso', curso),
    path('cursoDjango', cursoDjango),
]
