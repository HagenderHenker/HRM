from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Stellenarten, HHJGDE, Haushalte, Teilhaushalte, Produkte, Kostenstellen, Stellenplan, KostenstellenaufteilungStellen, StellenplanSoll, Stellenbesetzung
from .forms import StellenartenForm, HHJGDEForm, HaushalteForm, TeilhaushalteForm, ProdukteForm, KostenstellenForm

# Create your views here.

#CRUD Stellenarten model = Stellenarten

def stellenarten_uebersicht(request):
    
    stellenarten = Stellenarten.objects.all().order_by('stellenart')

    return render(request, 'stellenplan/stellenarten/stellenarten_uebersicht.html', {'stellenarten': stellenarten})
    




def stellenarten_add(request):

    if request.method == 'GET':
        form = StellenartenForm()
        return render(request, 'stellenplan/stellenarten/stellenarten_uebersicht.html#stellenarten_add_form', {'form': form})
    
    if request.method == 'POST':
        form = StellenartenForm(request.POST)

        if form.is_valid():
            print("form is valid")
            stellenart = form.save()
            if request.headers.get('HX-Request'):
                return render(request, 'stellenplan/stellenarten/stellenarten_uebersicht.html#stellenartentablerow', {'stellenart': stellenart})
            return redirect('stellenartenuebersicht')
        else:
            print("form is not valid")
            return HttpResponse('alles doof gelaufen')

    return render(request, 'stellenplan/stellenarten/stellenarten_uebersicht.html#stellenarten_add_form')


def stellenarten_edit(request, id):
    return HttpResponse(f"Stellenart mit ID {id} bearbeiten")



def stellenarten_delete(request, id):
    return HttpResponse(f"Stellenart mit ID {id} löschen")

# CRUD HHJGDE

def HHJGDE_uebersicht(request):
    return HttpResponse("HHJGDE Übersicht")

def HHJGDE_add(request):
    return HttpResponse("HHJGDE hinzufügen")

def HHJGDE_edit(request, id):
    return HttpResponse(f"HHJGDE mit ID {id} bearbeiten")

def HHJGDE_delete(request, id):
    return HttpResponse(f"HHJGDE mit ID {id} löschen")




# CRUD Haushalte

def haushalte_uebersicht(request):
    return HttpResponse("Haushaltsübersicht")

def haushalte_add(request):
    return HttpResponse("Haushalt hinzufügen")

def haushalte_edit(request, id):
    return HttpResponse(f"Haushalt mit ID {id} bearbeiten")

def haushalte_delete(request, id):
    return HttpResponse(f"Haushalt mit ID {id} löschen")

# CRUD Teilhaushalte model = Teilhaushalte

def teilhaushalte_uebersicht(request):
    return HttpResponse("Teilhaushaltsübersicht")

def teilhaushalte_add(request):
    return HttpResponse("Teilhaushalt hinzufügen")

def teilhaushalte_edit(request, id):
    return HttpResponse(f"Teilhaushalt mit ID {id} bearbeiten")

def teilhaushalte_delete(request, id):
    return HttpResponse(f"Teilhaushalt mit ID {id} löschen")

# CRUD Produkte model = Produkte

def produkte_uebersicht(request):
    return HttpResponse("Produktübersicht")

def produkte_add(request):
    return HttpResponse("Produkt hinzufügen")

def produkte_edit(request, id):
    return HttpResponse(f"Produkt mit ID {id} bearbeiten")

def produkte_delete(request, id):
    return HttpResponse(f"Produkt mit ID {id} löschen")

# CRUD Kostenstellen model = Kostenstellen

def kostenstellen_uebersicht(request):
    return HttpResponse("Kostenstellenübersicht")

def kostenstellen_add(request):
    return HttpResponse("Kostenstelle hinzufügen")

def kostenstellen_edit(request, id):
    return HttpResponse(f"Kostenstelle mit ID {id} bearbeiten")

def kostenstellen_delete(request, id):
    return HttpResponse(f"Kostenstelle mit ID {id} löschen")


# CRUD Stellenplan model = Stellenplan

def stellenuebersicht(request):
    return HttpResponse("Stellenübersicht")

def stellen_add(request):
    return HttpResponse("Stelle hinzufügen")

def stellen_edit(request, id):
    return HttpResponse(f"Stelle mit ID {id} bearbeiten")

def stellen_delete(request, id):
    return HttpResponse(f"Stelle mit ID {id} löschen")


# CRUD Kostenstellenaufteilung model = KostenstellenausteilungStellen

def kostenstellenausteilung_uebersicht(request):
    return HttpResponse("Kostenstellenausteilungsübersicht")

def kostenstellenausteilung_add(request):
    return HttpResponse("Kostenstellenausteilung hinzufügen")

def kostenstellenausteilung_edit(request, id):
    return HttpResponse(f"Kostenstellenausteilung mit ID {id} bearbeiten")

def kostenstellenausteilung_delete(request, id):
    return HttpResponse(f"Kostenstellenausteilung mit ID {id} löschen")

# CRUD Stellenplan Soll model = StellenplanSoll
def stellenplan_soll_uebersicht(request):
    return HttpResponse("Stellenplan Soll Übersicht")

def stellenplan_soll_add(request):
    return HttpResponse("Stellenplan Soll hinzufügen")

def stellenplan_soll_edit(request, id):
    return HttpResponse(f"Stellenplan Soll mit ID {id} bearbeiten")

def stellenplan_soll_delete(request, id):
    return HttpResponse(f"Stellenplan Soll mit ID {id} löschen")

# CRUD Stellenplan Ist model = StellenplanIst
def stellenplan_ist_uebersicht(request):
    return HttpResponse("Stellenplan Ist Übersicht")

def stellenplan_ist_add(request):
    return HttpResponse("Stellenplan Ist hinzufügen")

def stellenplan_ist_edit(request, id):
    return HttpResponse(f"Stellenplan Ist mit ID {id} bearbeiten")

def stellenplan_ist_delete(request, id):
    return HttpResponse(f"Stellenplan Ist mit ID {id} löschen")





