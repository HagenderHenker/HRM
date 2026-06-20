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
from . views import stellenarten_uebersicht, stellenarten_add, stellenarten_edit, stellenarten_delete
from . views import HHJGDE_uebersicht, HHJGDE_add, HHJGDE_edit, HHJGDE_delete
from . views import haushalte_uebersicht, haushalte_add, haushalte_edit, haushalte_delete
from . views import teilhaushalte_uebersicht, teilhaushalte_add, teilhaushalte_edit, teilhaushalte_delete, teilhaushalte_cancel
from . views import produkte_uebersicht, produkte_add, produkte_edit, produkte_delete
from . views import kostenstellen_uebersicht, kostenstellen_add, kostenstellen_edit, kostenstellen_delete
from . views import stellenuebersicht, stellen_add, stellen_edit, stellen_delete
from . views import kostenstellen_uebersicht, kostenstellen_add, kostenstellen_edit, kostenstellen_delete
from . views import stellenplan_soll_uebersicht, stellenplan_soll_add, stellenplan_soll_edit, stellenplan_soll_delete
from . views import stellenplan_ist_uebersicht, stellenplan_ist_add, stellenplan_ist_edit, stellenplan_ist_delete

urlpatterns = [
    # CRUD Stellenarten model = Stellenarten
    path('stellenarten/', stellenarten_uebersicht, name='stellenarten_uebersicht'),
    path('stellenarten/add/', stellenarten_add, name='stellenarten_add'),
    path('stellenarten/edit/<int:id>/', stellenarten_edit, name='stellenarten_edit'),
    path('stellenarten/delete/<int:id>/', stellenarten_delete, name='stellenarten_delete'),

    # CRUD HHJGDE
    path('hhjgde/', HHJGDE_uebersicht, name='hhjgde_uebersicht'),
    path('hhjgde/add/', HHJGDE_add, name='hhjgde_add'),
    path('hhjgde/edit/<int:id>/', HHJGDE_edit, name='hhjgde_edit'),
    path('hhjgde/delete/<int:id>/', HHJGDE_delete, name='hhjgde_delete'),

    # CRUD Haushalte
    path('haushalte/', haushalte_uebersicht, name='haushalte_uebersicht'),
    path('haushalte/add/', haushalte_add, name='haushalte_add'),   
    path('haushalte/edit/<int:id>/', haushalte_edit, name='haushalte_edit'),
    path('haushalte/delete/<int:id>/', haushalte_delete, name='haushalte_delete'),

    # CRUD Teilhaushalte model = Teilhaushalte
    path('teilhaushalte/', teilhaushalte_uebersicht, name='teilhaushalte_uebersicht'),
    path('teilhaushalte/add/', teilhaushalte_add, name='teilhaushalte_add'),
    path('teilhaushalte/edit/<int:id>/', teilhaushalte_edit, name='teilhaushalte_edit'),
    path('teilhaushalte/delete/<int:id>/', teilhaushalte_delete, name='teilhaushalte_delete'),
    path('teilhaushalte/cancel/<int:id>/', teilhaushalte_cancel, name='teilhaushalte_cancel'),
    
    # CRUD Produkte model = Produkte
    path('produkte/', produkte_uebersicht, name='produkte_uebersicht'),
    path('produkte/add/', produkte_add, name='produkte_add'),
    path('produkte/edit/<int:id>/', produkte_edit, name='produkte_edit'),
    path('produkte/delete/<int:id>/', produkte_delete, name='produkte_delete'),
    
    # CRUD Kostenstellen model = Kostenstellen
    path('kostenstellen/', kostenstellen_uebersicht, name='kostenstellen_uebersicht'),
    path('kostenstellen/add/', kostenstellen_add, name='kostenstellen_add'),
    path('kostenstellen/edit/<int:id>/', kostenstellen_edit, name='kostenstellen_edit'),
    path('kostenstellen/delete/<int:id>/', kostenstellen_delete, name='kostenstellen_delete'),
    
    # CRUD Stellen model = Stellen
    path('', stellenuebersicht, name='stellenuebersicht'),
    path('stellen/add/', stellen_add, name='stellen_add'),
    path('stellen/edit/<int:id>/', stellen_edit, name='stellen_edit'),  
    path('stellen/delete/<int:id>/', stellen_delete, name='stellen_delete'),
    
    # CRUD Stellenplan Soll model = Stellenplan_Soll
    path('stellenplan_soll/', stellenplan_soll_uebersicht, name='stellenplan_soll_uebersicht'),
    path('stellenplan_soll/add/', stellenplan_soll_add, name='stellenplan_soll_add'),
    path('stellenplan_soll/edit/<int:id>/', stellenplan_soll_edit, name='stellenplan_soll_edit'),
    path('stellenplan_soll/delete/<int:id>/', stellenplan_soll_delete, name='stellenplan_soll_delete'),
    
    # CRUD Stellenplan Ist model = Stellenplan_Ist
    path('stellenplan_ist/', stellenplan_ist_uebersicht, name='stellenplan_ist_uebersicht'),
    path('stellenplan_ist/add/', stellenplan_ist_add, name='stellenplan_ist_add'),
    path('stellenplan_ist/edit/<int:id>/', stellenplan_ist_edit, name='stellenplan_ist_edit'),
    path('stellenplan_ist/delete/<int:id>/', stellenplan_ist_delete, name='stellenplan_ist_delete'),    
]
