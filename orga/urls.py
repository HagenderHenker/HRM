"""
URL configuration for komstar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from . views import gemeindenuebersicht, gemeinde_neu, gemeinde_bearbeiten, gemeinde_loeschen 

urlpatterns = [
    path('', gemeindenuebersicht, name='gemeindenuebersicht'),
    path('neu/', gemeinde_neu, name='gemeinde_neu'),
    path('bearbeiten/<int:id>/', gemeinde_bearbeiten, name='gemeinde_bearbeiten'),
    path('loeschen/<int:id>/', gemeinde_loeschen, name='gemeinde_loeschen'),
]
