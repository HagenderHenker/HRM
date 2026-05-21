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
from . views import koerperschaftstypenuebersicht, koerperschaftstypen_add, koerperschaftstypen_edit, koerperschaftstypen_delete
from . views import gemeindenuebersicht, gemeinde_add, gemeinde_edit, gemeinde_delete
from . views import orggliederungstiefe_uebersicht, orggliederungstiefe_add, orggliederungstiefe_edit, orggliederungstiefe_delete
from . views import organisationseinheiten_uebersicht, organisationseinheiten_add, organisationseinheiten_edit, organisationseinheiten_delete
from . views import aufgaben_uebersicht, aufgaben_add, aufgaben_edit, aufgaben_delete
from . views import gvp_uebersicht, gvp_add, gvp_edit, gvp_delete
from . views import taetigkeitenorg_uebersicht, taetigkeitenorg_add, taetigkeitenorg_edit, taetigkeitenorg_delete

urlpatterns = [
    # CRUD Koerperschaftstypen
    path('koerperschaftstypen/', koerperschaftstypenuebersicht, name='koerperschaftstypenuebersicht'),
    path('koerperschaftstypen/add/', koerperschaftstypen_add, name='koerperschaftstypen_add'),
    path('koerperschaftstypen/edit/<int:id>/', koerperschaftstypen_edit, name='koerperschaftstypen_edit'),
    path('koerperschaftstypen/delete/<int:id>/', koerperschaftstypen_delete, name='koerperschaftstypen_delete'),

    # CRUD Gemeinden
    path('gemeinden/', gemeindenuebersicht, name='gemeindenuebersicht'),
    path('gemeinden/add/', gemeinde_add, name='gemeinde_add'),
    path('gemeinden/edit/<int:id>/', gemeinde_edit, name='gemeinde_edit'),
    path('gemeinden/delete/<int:id>/', gemeinde_delete, name='gemeinde_delete'),
    
    # CRUD OrgGliederungstiefe
    path('orggliederungstiefe/', orggliederungstiefe_uebersicht, name='orggliederungstiefe_uebersicht'),
    path('orggliederungstiefe/add/', orggliederungstiefe_add, name='orggliederungstiefe_add'),
    path('orggliederungstiefe/edit/<int:id>/', orggliederungstiefe_edit, name='orggliederungstiefe_edit'),
    path('orggliederungstiefe/delete/<int:id>/', orggliederungstiefe_delete, name='orggliederungstiefe_delete'),

    # CRUD Organsationseinheiten
    path('organisationseinheiten/', organisationseinheiten_uebersicht, name='organisationseinheiten_uebersicht'),
    path('organisationseinheiten/add/', organisationseinheiten_add, name='organisationseinheiten_add'),
    path('organisationseinheiten/edit/<int:id>/', organisationseinheiten_edit, name='organisationseinheiten_edit'),
    path('organisationseinheiten/delete/<int:id>/', organisationseinheiten_delete, name='organisationseinheiten_delete'),

    #CRUD AUfgaben
    path('aufgaben/', aufgaben_uebersicht, name='aufgaben_uebersicht'),
    path('aufgaben/add/', aufgaben_add, name='aufgaben_add'),
    path('aufgaben/edit/<int:id>/', aufgaben_edit, name='aufgaben_edit'),
    path('aufgaben/delete/<int:id>/', aufgaben_delete, name='aufgaben_delete'),
    
    # CRUD GVP model = GVP
    path('gvp/', gvp_uebersicht, name='gvp_uebersicht'),
    path('gvp/add/', gvp_add, name='gvp_add'),
    path('gvp/edit/<int:id>/', gvp_edit, name='gvp_edit'),
    path('gvp/delete/<int:id>/', gvp_delete, name='gvp_delete'),

    # CRUD Taetigkeiten Organisationseinheiten model = TaetigkeitenOrg
    path('taetigkeitenorg/', taetigkeitenorg_uebersicht, name='taetigkeitenorg_uebersicht'),
    path('taetigkeitenorg/add/', taetigkeitenorg_add, name='taetigkeitenorg_add'),
    path('taetigkeitenorg/edit/<int:id>/', taetigkeitenorg_edit, name='taetigkeitenorg_edit'),
    path('taetigkeitenorg/delete/<int:id>/', taetigkeitenorg_delete, name='taetigkeitenorg_delete'),
    
]   