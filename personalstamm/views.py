from django.http import HttpResponse
from django.shortcuts import render, redirect
from komstar.crud import BaseCRUDView, HtmxCrudMixin, ListView, CreateView, UpdateView, DeleteView, CancelView
from . models import Personalstamm, VergGrp, StundenVZAE, Tabellenentgelt, Beurteilungstypen, PersFortschritt, Kinder, AusWeiterbildung, Beurteilungen, Pruefungen, TaetigkeitenPersonal, PersSonst 
from .forms import VergGrpForm, StundenVZAEForm, TabellenentgeltForm, BeurteilungstypenForm, PersFortschrittForm, KinderForm, AusWeiterbildungForm, BeurteilungenForm, PruefungenForm, TaetigkeitenPersonalForm, PersSonstForm
# Create your views here.

# CRUD vergütungsgruppen model = VergGrp

class VergGrpConfig:
    model = VergGrp
    form_class = VergGrpForm
    context_object_name = 'vergrp'
    list_url_name = 'vergrp_ueb'
    template_name = 'verguetungsgruppen/verguetungsgruppen.html'
    partial_row = 'tablerow'
    partial_add = 'table_add'
    partial_edit = 'table_edit'
    partial_delete = 'delete_confirmation'
    title = 'Vergütungsgruppen'
    titlesingular = ' Vergütungsgruppe'
    list_url_name = 'verggrp_ueb'

class VergGrpListView(VergGrpConfig, ListView):
    pass   

class VergGrpCreateView(VergGrpConfig, CreateView):
    pass

class VergGrpUpdateView(VergGrpConfig, UpdateView):
    pass

class VergGrpDeleteView(VergGrpConfig, DeleteView):
    pass

class VergGrpCancelView(VergGrpConfig, CancelView):
    pass

def vergrp_ueb(request):
    return HttpResponse("Vergütungsgruppenübersicht")

def vergrp_add(request):
    return HttpResponse("Vergütungsgruppe hinzufügen")

def vergrp_edit(request, id):
    return HttpResponse(f"Vergütungsgruppe mit ID {id} bearbeiten")

def vergrp_delete(request, id):
    return HttpResponse(f"Vergütungsgruppe mit ID {id} löschen")

# CRUD Arbeitszeitstandardmodelle model = StundenVZAE

def StundenVZAE_ueb(request):
    return HttpResponse("Arbeitszeitstandardmodelle Übersicht")

def StundenVZAE_add(request):
    return HttpResponse("Arbeitszeitstandardmodell hinzufügen")

def StundenVZAE_edit(request, id):
    return HttpResponse(f"Arbeitszeitstandardmodell mit ID {id} bearbeiten")

def StundenVZAE_delete(request, id):
    return HttpResponse(f"Arbeitszeitstandardmodell mit ID {id} löschen")

# CRUD Tabellenentgelt  model = Tabellenentgelt

def Tabellenentgelt_ueb(request):
    return HttpResponse("Tabellenentgelt Übersicht")

def Tabellenentgelt_add(request):
    return HttpResponse("Tabellenentgelt hinzufügen")

def Tabellenentgelt_edit(request, id):
    return HttpResponse(f"Tabellenentgelt mit ID {id} bearbeiten")

def Tabellenentgelt_delete(request, id):
    return HttpResponse(f"Tabellenentgelt mit ID {id} löschen")

# CRUD Beurteilungstypen model = Beurteilungstypen

def Beurteilungstypen_ueb(request):
    return HttpResponse("Beurteilungstypen Übersicht")

def Beurteilungstypen_add(request):
    return HttpResponse("Beurteilungstyp hinzufügen")

def Beurteilungstypen_edit(request, id):
    return HttpResponse(f"Beurteilungstyp mit ID {id} bearbeiten")

def Beurteilungstypen_delete(request, id):
    return HttpResponse(f"Beurteilungstyp mit ID {id} löschen")


# CRUD Personalstamm model = Personalstamm

def personaluebersicht(request):
    return HttpResponse("Personalübersicht")

def personaladd(request):
    return HttpResponse("Personal hinzufügen")

def personaledit(request, id): 
    return HttpResponse(f"Personal mit ID {id} bearbeiten")

def personaldelete(request, id):
    return HttpResponse(f"Personal mit ID {id} löschen")

# CRUD PersFortschritt model = PersFortschritt

def persfortschritt_ueb(request):
    return HttpResponse("PersFortschritt Übersicht")

def persfortschritt_add(request):
    return HttpResponse("PersFortschritt hinzufügen")

def persfortschritt_edit(request, id):
    return HttpResponse(f"PersFortschritt mit ID {id} bearbeiten")

def persfortschritt_delete(request, id):
    return HttpResponse(f"PersFortschritt mit ID {id} löschen")

# CRUD Kinder model = Kinder

def kinder_ueb(request):
    return HttpResponse("Kinder Übersicht")

def kinder_add(request):
    return HttpResponse("Kind hinzufügen")

def kinder_edit(request, id):
    return HttpResponse(f"Kind mit ID {id} bearbeiten")

def kinder_delete(request, id):
    return HttpResponse(f"Kind mit ID {id} löschen")

#CRUD Aus und Weiterbildung model = AusWeiterbildung

def ausweiterbildung_ueb(request):
    return HttpResponse("Aus- und Weiterbildung Übersicht")

def ausweiterbildung_add(request):
    return HttpResponse("Aus- und Weiterbildung hinzufügen")

def ausweiterbildung_edit(request, id):
    return HttpResponse(f"Aus- und Weiterbildung mit ID {id} bearbeiten")

def ausweiterbildung_delete(request, id):
    return HttpResponse(f"Aus- und Weiterbildung mit ID {id} löschen")

# CRUD Beurteilungen model = Beurteilungen

def beurteilungen_ueb(request):
    return HttpResponse("Beurteilungen Übersicht")

def beurteilungen_add(request):
    return HttpResponse("Beurteilung hinzufügen")

def beurteilungen_edit(request, id):
    return HttpResponse(f"Beurteilung mit ID {id} bearbeiten")

def beurteilungen_delete(request, id):
    return HttpResponse(f"Beurteilung mit ID {id} löschen")

# CRUD prüfungen model = Prüfungen 

def pruefungen_ueb(request):
    return HttpResponse("Prüfungen Übersicht")

def pruefungen_add(request):
    return HttpResponse("Prüfung hinzufügen")

def pruefungen_edit(request, id):
    return HttpResponse(f"Prüfung mit ID {id} bearbeiten")

def pruefungen_delete(request, id):
    return HttpResponse(f"Prüfung mit ID {id} löschen")

# CRUD Tätigkeiten des Personals model = TaetigkeitenPers

def taetigkeitenpers_ueb(request):
    return HttpResponse("Tätigkeiten des Personals Übersicht")

def taetigkeitenpers_add(request): 
    return HttpResponse("Tätigkeit des Personals hinzufügen")

def taetigkeitenpers_edit(request, id):
    return HttpResponse(f"Tätigkeit des Personals mit ID {id} bearbeiten")

def taetigkeitenpers_delete(request, id):
    return HttpResponse(f"Tätigkeit des Personals mit ID {id} löschen")

# CRUD Personal Sonstiges model = PersonalSonst

def personalsonst_ueb(request):
    return HttpResponse("Personal Sonstiges Übersicht")

def personalsonst_add(request):
    return HttpResponse("Personal Sonstiges hinzufügen")

def personalsonst_edit(request, id):
    return HttpResponse(f"Personal Sonstiges mit ID {id} bearbeiten")

def personalsonst_delete(request, id):
    return HttpResponse(f"Personal Sonstiges mit ID {id} löschen")