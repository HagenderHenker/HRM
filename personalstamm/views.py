from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from komstar.crud import BaseCRUDView, HtmxCrudMixin, ListView, CreateView, UpdateView, DeleteView, CancelView
from . models import Personalstamm, VergGrp, StundenVZAE, Tabellenentgelt, Beurteilungstypen, PersFortschritt, Kinder, AusWeiterbildung, Beurteilungen, Pruefungen, TaetigkeitenPersonal, PersSonst 
from .forms import VergGrpForm, StundenVZAEForm, TabellenentgeltForm, BeurteilungstypenForm, PersFortschrittForm, KinderForm, AusWeiterbildungForm, BeurteilungenForm, PruefungenForm, TaetigkeitenPersonalForm, PersSonstForm, PersonalstammForm, PersonalstammForm_shortened
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
    order_by = 'reihenfolge'
    
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

#def vergrp_ueb(request):
#    return HttpResponse("Vergütungsgruppenübersicht")

#def vergrp_add(request):
#    return HttpResponse("Vergütungsgruppe hinzufügen")

#def vergrp_edit(request, id):
 #   return HttpResponse(f"Vergütungsgruppe mit ID {id} bearbeiten")

#def vergrp_delete(request, id):
#    return HttpResponse(f"Vergütungsgruppe mit ID {id} löschen")

# CRUD Arbeitszeitstandardmodelle model = StundenVZAE

class StundenVZAEConfig:
    model = StundenVZAE
    form_class = StundenVZAEForm
    context_object_name = 'StundenVZAE'
    list_url_name = 'stundenvzae_ueb'
    template_name = 'arbeitszeitstandardmodelle/arbeitszeitstandardmodelle.html'
    partial_row = 'tablerow'
    partial_add = 'table_add'
    partial_edit = 'table_edit'
    partial_delete = 'delete_confirmation'
    title = 'Arbeitszeitstandardmodelle'
    titlesingular = 'Arbeitszeitstandardmodell'
    list_url_name = 'stundenvzae_ueb'
    order_by = 'art'
    
class StundenVZAEListView(StundenVZAEConfig, ListView):
    pass   

class StundenVZAECreateView(StundenVZAEConfig, CreateView):
    pass

class StundenVZAEUpdateView(StundenVZAEConfig, UpdateView):
    pass

class StundenVZAEDeleteView(StundenVZAEConfig, DeleteView):
    pass

class StundenVZAECancelView(StundenVZAEConfig, CancelView):
    pass


#def StundenVZAE_ueb(request):
#    return HttpResponse("Arbeitszeitstandardmodelle Übersicht")

#def StundenVZAE_add(request):
#    return HttpResponse("Arbeitszeitstandardmodell hinzufügen")

#def StundenVZAE_edit(request, id):
#    return HttpResponse(f"Arbeitszeitstandardmodell mit ID {id} bearbeiten")

#def StundenVZAE_delete(request, id):
#    return HttpResponse(f"Arbeitszeitstandardmodell mit ID {id} löschen")

# CRUD Tabellenentgelt  model = Tabellenentgelt

class TabellenentgeltConfig:
    model = Tabellenentgelt
    form_class = TabellenentgeltForm
    context_object_name = 'Tabellenentgelt'
    list_url_name = 'tabellenentgelt_ueb'
    template_name = 'tabellenentgelt/tabellenentgelt.html'
    partial_row = 'tablerow'
    partial_add = 'table_add'
    partial_edit = 'table_edit'
    partial_delete = 'delete_confirmation'
    title = 'Tabellenentgelt'
    titlesingular = 'Tabellenentgelt'
   
    order_by = 'verg_grp'

class TabellenentgeltListView(TabellenentgeltConfig, ListView):
    pass

class TabellenentgeltCreateView(TabellenentgeltConfig, CreateView):
    pass

class TabellenentgeltUpdateView(TabellenentgeltConfig, UpdateView):
    pass

class TabellenentgeltDeleteView(TabellenentgeltConfig, DeleteView):
    pass

class TabellenentgeltCancelView(TabellenentgeltConfig, CancelView):
    pass

#def Tabellenentgelt_ueb(request):
#    return HttpResponse("Tabellenentgelt Übersicht")

#def Tabellenentgelt_add(request):
#    return HttpResponse("Tabellenentgelt hinzufügen")

#def Tabellenentgelt_edit(request, id):
#    return HttpResponse(f"Tabellenentgelt mit ID {id} bearbeiten")

#def Tabellenentgelt_delete(request, id):
#    return HttpResponse(f"Tabellenentgelt mit ID {id} löschen")

# CRUD Beurteilungstypen model = Beurteilungstypen

class BeurteilungstypenConfig:
    model = Beurteilungstypen
    form_class = BeurteilungstypenForm
    context_object_name = 'Beurteilungstypen'
    list_url_name = 'beurteilungstypen_ueb'
    template_name = 'beurteilungstypen/beurteilungstypen.html'
    partial_row = 'tablerow'
    partial_add = 'table_add'
    partial_edit = 'table_edit'
    partial_delete = 'delete_confirmation'
    title = 'Beurteilungstypen'
    titlesingular = 'Beurteilungstyp'
   
    order_by = 'verg_grp'

class BeurteilungstypenListView(BeurteilungstypenConfig, ListView):
    pass

class BeurteilungstypenCreateView(BeurteilungstypenConfig, CreateView):
    pass

class BeurteilungstypenUpdateView(BeurteilungstypenConfig, UpdateView):
    pass

class BeurteilungstypenDeleteView(BeurteilungstypenConfig, DeleteView):
    pass

class BeurteilungstypenCancelView(BeurteilungstypenConfig, CancelView):
    pass

#def Beurteilungstypen_ueb(request):
#    return HttpResponse("Beurteilungstypen Übersicht")

#def Beurteilungstypen_add(request):
#    return HttpResponse("Beurteilungstyp hinzufügen")

#def Beurteilungstypen_edit(request, id):
#    return HttpResponse(f"Beurteilungstyp mit ID {id} bearbeiten")#

#def Beurteilungstypen_delete(request, id):
#    return HttpResponse(f"Beurteilungstyp mit ID {id} löschen")


#-----------------------------------------------
# Personalstammdaten 
#-----------------------------------------------



"""
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
    return HttpResponse(f"Personal Sonstiges mit ID {id} löschen")"""


# ============================================================
# Personalstammdaten
# ============================================================


# --- CRUD Personalstamm model = Personalstamm --------------

def personaluebersicht(request):
    """
    Rendert immer die vollständige Seite. Die Suchleiste im Template
    nutzt hx-select="#personal-tbody", um sich aus dieser Antwort nur
    den Tabellenkörper herauszuschneiden - daher keine htmx/non-htmx
    Verzweigung nötig.
    """
    q = request.GET.get('q', '').strip()

    qs = Personalstamm.objects.select_related('gemeinde').order_by('nachname', 'vorname')

    if q:
        if q.isdigit():
            qs = qs.filter(pers_nr=int(q))
        else:
            qs = qs.filter(Q(nachname__icontains=q) | Q(vorname__icontains=q))

    context = {
        'title': 'Personalübersicht',
        'personal_list': qs,
        'q': q,
    }
    return render(request, 'personalstamm/personaluebersicht.html', context)


def personal_row_detail(request, pers_nr):
    """
    Lazy-Load-Endpunkt für den Akkordeon-Detailbereich einer Mitarbeiterzeile.
    Wird nur einmalig pro Seitenaufruf angefragt
    (hx-trigger="toggle[target.open] once" im Template).
    """
    p = get_object_or_404(Personalstamm.objects.select_related('gemeinde'), pers_nr=pers_nr)

    context = {
        'p': p,
        'kinder': p.kinder_set.all(),
        'fortschritt': p.persfortschritt_set.order_by('-ab_datum'),
        'ausbildung': p.ausweiterbildung_set.all(),
        'beurteilungen': p.beurteilungen_set.select_related('beurteilungstyp'),
        'pruefungen': p.pruefungen_set.all(),
        'taetigkeiten': p.taetigkeitenpersonal_set.all(),
        'sonstiges': p.perssonst_set.all(),
    }
    return render(request, 'personalstamm/personaluebersicht.html#row_detail', context)


def personaladd(request):
   
    """
    GET  -> liefert das leere Modal-Formular.
    POST -> validiert und legt den Mitarbeiter an.
 
    Bei Erfolg wird das Modal geschlossen (leeres #modal-Fragment)
    und der Response-Header HX-Trigger gesetzt. Das Suchfeld in
    personaluebersicht.html kann darauf per
    'hx-trigger="..., personal-added from:body"' reagieren und
    die Liste automatisch neu laden.
    """

    if request.method == 'POST':
        form = PersonalstammForm(request.POST)
        if form.is_valid():
            form.save()
            response = render(request, 'personalstamm/personaluebersicht.html#modal_close', {})
            response['HX-Trigger'] = 'personal-added'
            return response
        # Ungültig -> Modal mit Fehlermeldungen erneut anzeigen
        return render(request, 'personalstamm/personaluebersicht.html#personal_add_modal', {'form': form})
 
    form = PersonalstammForm()
    return render(request, 'personalstamm/personaluebersicht.html#personal_add_modal', {'form': form})
 
 
def personal_modal_close(request):
    """Wird vom 'Abbrechen'-Link im Modal aufgerufen und leert #modal."""
    return render(request, 'personalstamm/personaluebersicht.html#modal_close', {})

def personal_row_detail(request, pers_nr):
    """
    Lazy-Load-Endpunkt für den Akkordeon-Detailbereich einer Mitarbeiterzeile.
    Wird nur einmalig pro Seitenaufruf angefragt
    (hx-trigger="toggle[target.open] once" im Template).
    """
    p = get_object_or_404(Personalstamm.objects.select_related('gemeinde'), pers_nr=pers_nr)

    context = {
        'p': p,
        'kinder': p.kinder_set.all(),
        'fortschritt': p.persfortschritt_set.order_by('-ab_datum'),
        'ausbildung': p.ausweiterbildung_set.all(),
        'beurteilungen': p.beurteilungen_set.select_related('beurteilungstyp'),
        'pruefungen': p.pruefungen_set.all(),
        'taetigkeiten': p.taetigkeitenpersonal_set.all(),
        'sonstiges': p.perssonst_set.all(),
    }
    return render(request, 'personalstamm/personaluebersicht.html#row_detail', context)


def personaledit(request, id):
    return HttpResponse(f"Personal mit ID {id} bearbeiten")


def personaldelete(request, id):
    return HttpResponse(f"Personal mit ID {id} löschen")


# --- CRUD PersFortschritt model = PersFortschritt -----------

def persfortschritt_add(request, pers_nr):
    pers = get_object_or_404(Personalstamm, pers_nr=pers_nr)

    if request.method == 'POST':
        form = PersFortschrittForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.pers_nr = pers
            row.save()
            return render(request, 'personalstamm/personaluebersicht.html#persfortschritt_tablerow', {'row': row})
        return render(
            request,
            'personalstamm/personaluebersicht.html#persfortschritt_row_add',
            {'form': form, 'pers_nr': pers.pers_nr},
        )

    form = PersFortschrittForm()
    return render(
        request,
        'personalstamm/personaluebersicht.html#persfortschritt_row_add',
        {'form': form, 'pers_nr': pers.pers_nr},
    )


def persfortschritt_edit(request, id):
    row = get_object_or_404(PersFortschritt, id=id)

    if request.method == 'POST':
        form = PersFortschrittForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            return render(request, 'personalstamm/personaluebersicht.html#persfortschritt_tablerow', {'row': row})
        return render(request, 'personalstamm/personaluebersicht.html#persfortschritt_row_edit', {'form': form})

    form = PersFortschrittForm(instance=row)
    return render(request, 'personalstamm/personaluebersicht.html#persfortschritt_row_edit', {'form': form})


def persfortschritt_delete(request, id):
    row = get_object_or_404(PersFortschritt, id=id)

    if request.method == 'POST':
        row.delete()
        return HttpResponse('')

    return render(request, 'personalstamm/personaluebersicht.html#persfortschritt_delete_confirm', {'row': row})


def persfortschritt_cancel(request, id):
    row = get_object_or_404(PersFortschritt, id=id)
    return render(request, 'personalstamm/personaluebersicht.html#persfortschritt_tablerow', {'row': row})


# --- CRUD Kinder model = Kinder ------------------------------

def kinder_add(request, pers_nr):
    pers = get_object_or_404(Personalstamm, pers_nr=pers_nr)
    print(pers)

    if request.method == 'POST':
        #print(request.POST)
        form = KinderForm(request.POST)
        form.pers_nr = pers  # Setze die pers_nr auf das Personalstamm-Objekt
        #print(form)
        if form.is_valid():
            print("Form is valid")
            row = form.save(commit=False)
            row.pers_nr = pers
            row.save()
            return render(request, 'personalstamm/personaluebersicht.html#kinder_tablerow', {'row': row})
        else:
            print("Form errors:", form.errors)

        print("Form is not valid")
        return render(
            request,
            'personalstamm/personaluebersicht.html#kinder_row_add',
            {'form': form, 'pers_nr': pers.pers_nr},
        )

    form = KinderForm()
    return render(
        request,
        'personalstamm/personaluebersicht.html#kinder_row_add',
        {'form': form, 'pers_nr': pers.pers_nr},
    )


def kinder_edit(request, id):
    row = get_object_or_404(Kinder, id=id)

    if request.method == 'POST':
        form = KinderForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            return render(request, 'personalstamm/personaluebersicht.html#kinder_tablerow', {'row': row})
        return render(request, 'personalstamm/personaluebersicht.html#kinder_row_edit', {'form': form})

    form = KinderForm(instance=row)
    return render(request, 'personalstamm/personaluebersicht.html#kinder_row_edit', {'form': form})


def kinder_delete(request, id):
    row = get_object_or_404(Kinder, id=id)

    if request.method == 'POST':
        row.delete()
        return HttpResponse('')

    return render(request, 'personalstamm/personaluebersicht.html#kinder_delete_confirm', {'row': row})


def kinder_cancel(request, id):
    row = get_object_or_404(Kinder, id=id)
    return render(request, 'personalstamm/personaluebersicht.html#kinder_tablerow', {'row': row})


# --- CRUD Aus- und Weiterbildung model = AusWeiterbildung ----

def ausweiterbildung_add(request, pers_nr):
    pers = get_object_or_404(Personalstamm, pers_nr=pers_nr)

    if request.method == 'POST':
        form = AusWeiterbildungForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.pers_nr = pers
            row.save()
            return render(request, 'personalstamm/personaluebersicht.html#ausweiterbildung_tablerow', {'row': row})
        return render(
            request,
            'personalstamm/personaluebersicht.html#ausweiterbildung_row_add',
            {'form': form, 'pers_nr': pers.pers_nr},
        )

    form = AusWeiterbildungForm()
    return render(
        request,
        'personalstamm/personaluebersicht.html#ausweiterbildung_row_add',
        {'form': form, 'pers_nr': pers.pers_nr},
    )


def ausweiterbildung_edit(request, id):
    row = get_object_or_404(AusWeiterbildung, id=id)

    if request.method == 'POST':
        form = AusWeiterbildungForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            return render(request, 'personalstamm/personaluebersicht.html#ausweiterbildung_tablerow', {'row': row})
        return render(request, 'personalstamm/personaluebersicht.html#ausweiterbildung_row_edit', {'form': form})

    form = AusWeiterbildungForm(instance=row)
    return render(request, 'personalstamm/personaluebersicht.html#ausweiterbildung_row_edit', {'form': form})


def ausweiterbildung_delete(request, id):
    row = get_object_or_404(AusWeiterbildung, id=id)

    if request.method == 'POST':
        row.delete()
        return HttpResponse('')

    return render(request, 'personalstamm/personaluebersicht.html#ausweiterbildung_delete_confirm', {'row': row})


def ausweiterbildung_cancel(request, id):
    row = get_object_or_404(AusWeiterbildung, id=id)
    return render(request, 'personalstamm/personaluebersicht.html#ausweiterbildung_tablerow', {'row': row})


# --- CRUD Beurteilungen model = Beurteilungen ----------------

def beurteilungen_add(request, pers_nr):
    pers = get_object_or_404(Personalstamm, pers_nr=pers_nr)

    if request.method == 'POST':
        form = BeurteilungenForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.pers_nr = pers
            row.save()
            return render(request, 'personalstamm/personaluebersicht.html#beurteilungen_tablerow', {'row': row})
        return render(
            request,
            'personalstamm/personaluebersicht.html#beurteilungen_row_add',
            {'form': form, 'pers_nr': pers.pers_nr},
        )

    form = BeurteilungenForm()
    return render(
        request,
        'personalstamm/personaluebersicht.html#beurteilungen_row_add',
        {'form': form, 'pers_nr': pers.pers_nr},
    )


def beurteilungen_edit(request, id):
    row = get_object_or_404(Beurteilungen, id=id)

    if request.method == 'POST':
        form = BeurteilungenForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            return render(request, 'personalstamm/personaluebersicht.html#beurteilungen_tablerow', {'row': row})
        return render(request, 'personalstamm/personaluebersicht.html#beurteilungen_row_edit', {'form': form})

    form = BeurteilungenForm(instance=row)
    return render(request, 'personalstamm/personaluebersicht.html#beurteilungen_row_edit', {'form': form})


def beurteilungen_delete(request, id):
    row = get_object_or_404(Beurteilungen, id=id)

    if request.method == 'POST':
        row.delete()
        return HttpResponse('')

    return render(request, 'personalstamm/personaluebersicht.html#beurteilungen_delete_confirm', {'row': row})


def beurteilungen_cancel(request, id):
    row = get_object_or_404(Beurteilungen, id=id)
    return render(request, 'personalstamm/personaluebersicht.html#beurteilungen_tablerow', {'row': row})


# --- CRUD Prüfungen model = Pruefungen -----------------------
# Achtung: 'zeugnis' ist ein FileField -> request.FILES muss mitgegeben
# werden, und das <form> im Template braucht enctype="multipart/form-data".

def pruefungen_add(request, pers_nr):
    pers = get_object_or_404(Personalstamm, pers_nr=pers_nr)

    if request.method == 'POST':
        form = PruefungenForm(request.POST, request.FILES)
        if form.is_valid():
            row = form.save(commit=False)
            row.pers_nr = pers
            row.save()
            return render(request, 'personalstamm/personaluebersicht.html#pruefungen_tablerow', {'row': row})
        return render(
            request,
            'personalstamm/personaluebersicht.html#pruefungen_row_add',
            {'form': form, 'pers_nr': pers.pers_nr},
        )

    form = PruefungenForm()
    return render(
        request,
        'personalstamm/personaluebersicht.html#pruefungen_row_add',
        {'form': form, 'pers_nr': pers.pers_nr},
    )


def pruefungen_edit(request, id):
    row = get_object_or_404(Pruefungen, id=id)

    if request.method == 'POST':
        form = PruefungenForm(request.POST, request.FILES, instance=row)
        if form.is_valid():
            form.save()
            return render(request, 'personalstamm/personaluebersicht.html#pruefungen_tablerow', {'row': row})
        return render(request, 'personalstamm/personaluebersicht.html#pruefungen_row_edit', {'form': form})

    form = PruefungenForm(instance=row)
    return render(request, 'personalstamm/personaluebersicht.html#pruefungen_row_edit', {'form': form})


def pruefungen_delete(request, id):
    row = get_object_or_404(Pruefungen, id=id)

    if request.method == 'POST':
        row.delete()
        return HttpResponse('')

    return render(request, 'personalstamm/personaluebersicht.html#pruefungen_delete_confirm', {'row': row})


def pruefungen_cancel(request, id):
    row = get_object_or_404(Pruefungen, id=id)
    return render(request, 'personalstamm/personaluebersicht.html#pruefungen_tablerow', {'row': row})


# --- CRUD Tätigkeiten Personal model = TaetigkeitenPersonal --

def taetigkeitenpers_add(request, pers_nr):
    pers = get_object_or_404(Personalstamm, pers_nr=pers_nr)

    if request.method == 'POST':
        form = TaetigkeitenPersonalForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.pers_nr = pers
            row.save()
            return render(request, 'personalstamm/personaluebersicht.html#taetigkeitenpers_tablerow', {'row': row})
        return render(
            request,
            'personalstamm/personaluebersicht.html#taetigkeitenpers_row_add',
            {'form': form, 'pers_nr': pers.pers_nr},
        )

    form = TaetigkeitenPersonalForm()
    return render(
        request,
        'personalstamm/personaluebersicht.html#taetigkeitenpers_row_add',
        {'form': form, 'pers_nr': pers.pers_nr},
    )


def taetigkeitenpers_edit(request, id):
    row = get_object_or_404(TaetigkeitenPersonal, id=id)

    if request.method == 'POST':
        form = TaetigkeitenPersonalForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            return render(request, 'personalstamm/personaluebersicht.html#taetigkeitenpers_tablerow', {'row': row})
        return render(request, 'personalstamm/personaluebersicht.html#taetigkeitenpers_row_edit', {'form': form})

    form = TaetigkeitenPersonalForm(instance=row)
    return render(request, 'personalstamm/personaluebersicht.html#taetigkeitenpers_row_edit', {'form': form})


def taetigkeitenpers_delete(request, id):
    row = get_object_or_404(TaetigkeitenPersonal, id=id)

    if request.method == 'POST':
        row.delete()
        return HttpResponse('')

    return render(request, 'personalstamm/personaluebersicht.html#taetigkeitenpers_delete_confirm', {'row': row})


def taetigkeitenpers_cancel(request, id):
    row = get_object_or_404(TaetigkeitenPersonal, id=id)
    return render(request, 'personalstamm/personaluebersicht.html#taetigkeitenpers_tablerow', {'row': row})


# --- CRUD Personal Sonstiges model = PersSonst ---------------

def personalsonst_add(request, pers_nr):
    pers = get_object_or_404(Personalstamm, pers_nr=pers_nr)

    if request.method == 'POST':
        form = PersSonstForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.pers_nr = pers
            row.save()
            return render(request, 'personalstamm/personaluebersicht.html#personalsonst_tablerow', {'row': row})
        return render(
            request,
            'personalstamm/personaluebersicht.html#personalsonst_row_add',
            {'form': form, 'pers_nr': pers.pers_nr},
        )

    form = PersSonstForm()
    return render(
        request,
        'personalstamm/personaluebersicht.html#personalsonst_row_add',
        {'form': form, 'pers_nr': pers.pers_nr},
    )


def personalsonst_edit(request, id):
    row = get_object_or_404(PersSonst, id=id)

    if request.method == 'POST':
        form = PersSonstForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            return render(request, 'personalstamm/personaluebersicht.html#personalsonst_tablerow', {'row': row})
        return render(request, 'personalstamm/personaluebersicht.html#personalsonst_row_edit', {'form': form})

    form = PersSonstForm(instance=row)
    return render(request, 'personalstamm/personaluebersicht.html#personalsonst_row_edit', {'form': form})


def personalsonst_delete(request, id):
    row = get_object_or_404(PersSonst, id=id)

    if request.method == 'POST':
        row.delete()
        return HttpResponse('')

    return render(request, 'personalstamm/personaluebersicht.html#personalsonst_delete_confirm', {'row': row})


def personalsonst_cancel(request, id):
    row = get_object_or_404(PersSonst, id=id)
    return render(request, 'personalstamm/personaluebersicht.html#personalsonst_tablerow', {'row': row})