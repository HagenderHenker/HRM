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
from . views import personaluebersicht, personaladd, personaledit, personaldelete
from . views import VergGrpListView, VergGrpCreateView, VergGrpUpdateView, VergGrpDeleteView, VergGrpCancelView
#from . views import vergrp_ueb, vergrp_add, vergrp_edit, vergrp_delete
from . views import StundenVZAEListView, StundenVZAECreateView, StundenVZAEUpdateView, StundenVZAEDeleteView, StundenVZAECancelView
#from . views import StundenVZAE_ueb, StundenVZAE_add, StundenVZAE_edit, StundenVZAE_delete
from . views import TabellenentgeltListView, TabellenentgeltCreateView, TabellenentgeltUpdateView, TabellenentgeltDeleteView, TabellenentgeltCancelView
#from . views import Tabellenentgelt_ueb, Tabellenentgelt_add, Tabellenentgelt_edit, Tabellenentgelt_delete
from . views import Beurteilungstypen_ueb, Beurteilungstypen_add, Beurteilungstypen_edit, Beurteilungstypen_delete
from . views import persfortschritt_ueb, persfortschritt_add, persfortschritt_edit, persfortschritt_delete
from . views import kinder_ueb, kinder_add, kinder_edit, kinder_delete
from . views import ausweiterbildung_ueb, ausweiterbildung_add, ausweiterbildung_edit, ausweiterbildung_delete
from . views import beurteilungen_ueb, beurteilungen_add, beurteilungen_edit, beurteilungen_delete
from . views import pruefungen_ueb, pruefungen_add, pruefungen_edit, pruefungen_delete
from . views import taetigkeitenpers_ueb, taetigkeitenpers_add, taetigkeitenpers_edit, taetigkeitenpers_delete
from . views import personalsonst_ueb, personalsonst_add, personalsonst_edit, personalsonst_delete


urlpatterns = [
    path('', personaluebersicht, name='personaluebersicht'),
    path('admin/', admin.site.urls),
    path('pers/add/', personaladd, name='personaladd'),
    path('pers/edit/<int:id>/', personaledit, name='personaledit'),
    path('pers/delete/<int:id>/', personaldelete, name='personaldelete'),
    

    # CRUD Vergütungsgruppen model = VerGrp
#    path('vergrp/', vergrp_ueb, name='vergrp_ueb'),
#    path('vergrp/add/', vergrp_add, name='vergrp_add'),
#    path('vergrp/edit/<int:id>/', vergrp_edit, name='vergrp_edit'),
#    path('vergrp/delete/<int:id>/', vergrp_delete, name='vergrp_delete'),
    
    path('verggrp/', VergGrpListView.as_view(), name='verggrp_ueb'),
    path('verggrp/add/', VergGrpCreateView.as_view(), name='verggrp_add'),
    path('verggrp/edit/<int:id>/', VergGrpUpdateView.as_view(), name='verggrp_edit'),
    path('verggrp/delete/<int:id>/', VergGrpDeleteView.as_view(), name='verggrp_delete'),
    path('verggrp/cancel/<int:id>/', VergGrpCancelView.as_view(), name='verggrp_cancel'),
    






    # CRUD Arbeitszeitstandardmodelle model = StundenVZAE
    #path('stundenvzae/', StundenVZAE_ueb, name='stundenvzae_ueb'),
    #path('stundenvzae/add/', StundenVZAE_add, name='stundenvzae_add'),
    #path('stundenvzae/edit/<int:id>/', StundenVZAE_edit, name='stundenvzae_edit'),
    #path('stundenvzae/delete/<int:id>/', StundenVZAE_delete, name='stundenvzae_delete'),

    path('stundenvzae/', StundenVZAEListView.as_view(), name='stundenvzae_ueb'),
    path('stundenvzae/add/', StundenVZAECreateView.as_view(), name='stundenvzae_add'),  
    path('stundenvzae/edit/<int:id>/', StundenVZAEUpdateView.as_view(), name='stundenvzae_edit'),
    path('stundenvzae/delete/<int:id>/', StundenVZAEDeleteView.as_view(), name='stundenvzae_delete'),
    path('stundenvzae/cancel/<int:id>/', StundenVZAECancelView.as_view(), name='stundenvzae_cancel'),


    # CRUD Tabellenentgelt  model = Tabellenentgelt
    
    path('tabellenentgelt/', TabellenentgeltListView.as_view(), name='tabellenentgelt_ueb'),
    path('tabellenentgelt/add/', TabellenentgeltCreateView.as_view(), name='tabellenentgelt_add'),
    path('tabellenentgelt/edit/<int:id>/', TabellenentgeltUpdateView.as_view(), name='tabellenentgelt_edit'),
    path('tabellenentgelt/delete/<int:id>/', TabellenentgeltDeleteView.as_view(), name='tabellenentgelt_delete'),
    path('tabellenentgelt/cancel/<int:id>/', TabellenentgeltCancelView.as_view(), name='tabellenentgelt_cancel'),
       
    
    
    #path('tabellenentgelt/', Tabellenentgelt_ueb, name='tabellenentgelt_ueb'),
    #path('tabellenentgelt/add/', Tabellenentgelt_add, name='tabellenentgelt_add'),
    #path('tabellenentgelt/edit/<int:id>/', Tabellenentgelt_edit, name='tabellenentgelt_edit'),
    #path('tabellenentgelt/delete/<int:id>/', Tabellenentgelt_delete, name='tabellenentgelt_delete'),

    # CRUD Beurteilungstypen model = Beurteilungstypen
    path('beurteilungstypen/', Beurteilungstypen_ueb, name='beurteilungstypen_ueb'),
    path('beurteilungstypen/add/', Beurteilungstypen_add, name='beurteilungstypen_add'),
    path('beurteilungstypen/edit/<int:id>/', Beurteilungstypen_edit, name='beurteilungstypen_edit'),
    path('beurteilungstypen/delete/<int:id>/', Beurteilungstypen_delete, name='beurteilungstypen_delete'),

    # CRUD Personal Fortschritt model = PersFortschritt
    path('persfortschritt/', persfortschritt_ueb, name='persfortschritt_ueb'),
    path('persfortschritt/add/', persfortschritt_add, name='persfortschritt_add'),
    path('persfortschritt/edit/<int:id>/', persfortschritt_edit, name='persfortschritt_edit'),
    path('persfortschritt/delete/<int:id>/', persfortschritt_delete, name='persfortschritt_delete'),

    # CRUD Kinder model = Kinder
    path('kinder/', kinder_ueb, name='kinder_ueb'),
    path('kinder/add/', kinder_add, name='kinder_add'),
    path('kinder/edit/<int:id>/', kinder_edit, name='kinder_edit'),
    path('kinder/delete/<int:id>/', kinder_delete, name='kinder_delete'),

    # CRUD Aus- und Weiterbildung model = Ausweiterbildung
    path('ausweiterbildung/', ausweiterbildung_ueb, name='ausweiterbildung_ueb'),
    path('ausweiterbildung/add/', ausweiterbildung_add, name='ausweiterbildung_add'),
    path('ausweiterbildung/edit/<int:id>/', ausweiterbildung_edit, name='ausweiterbildung_edit'),
    path('ausweiterbildung/delete/<int:id>/', ausweiterbildung_delete, name='ausweiterbildung_delete'),

    # CRUD Beurteilungen model = Beurteilungen

    path('beurteilungen/', beurteilungen_ueb, name='beurteilungen_ueb'),
    path('beurteilungen/add/', beurteilungen_add, name='beurteilungen_add'),
    path('beurteilungen/edit/<int:id>/', beurteilungen_edit, name='beurteilungen_edit'),
    path('beurteilungen/delete/<int:id>/', beurteilungen_delete, name='beurteilungen_delete'),
    
    # CRUD Prüfungen model = Prüfungen
    path('pruefungen/', pruefungen_ueb, name='pruefungen_ueb'),
    path('pruefungen/add/', pruefungen_add, name='pruefungen_add'),
    path('pruefungen/edit/<int:id>/', pruefungen_edit, name='pruefungen_edit'),
    path('pruefungen/delete/<int:id>/', pruefungen_delete, name='pruefungen_delete'),   

    # CRUD Tätigkeiten Personal model = TaetigkeitenPers
    path('taetigkeitenpers/', taetigkeitenpers_ueb, name='taetigkeitenpers_ueb'),
    path('taetigkeitenpers/add/', taetigkeitenpers_add, name='taetigkeitenpers_add'),
    path('taetigkeitenpers/edit/<int:id>/', taetigkeitenpers_edit, name='taetigkeitenpers_edit'),
    path('taetigkeitenpers/delete/<int:id>/', taetigkeitenpers_delete, name='taetigkeitenpers_delete'),

    # CRUD Personal Sonstiges model = Personalsonst
    path('personalsonst/', personalsonst_ueb, name='personalsonst_ueb'),
    path('personalsonst/add/', personalsonst_add, name='personalsonst_add'),
    path('personalsonst/edit/<int:id>/', personalsonst_edit, name='personalsonst_edit'),
    path('personalsonst/delete/<int:id>/', personalsonst_delete, name='personalsonst_delete'), 

    
]
