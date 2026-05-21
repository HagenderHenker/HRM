from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Gemeinden, OrgGliederungstiefe, Organisationseinheiten, Aufgaben, Geschaeftsverteilung, TaetigkeitenORG
from .forms import GemeindenForm, KoerperschaftstypenForm


# Create your views here.

# CRUD Koerperschaftstypen

def koerperschaftstypenuebersicht(request):
    return render(request, 'orga/koerperschaftstypen/koerperschaftstypen_uebersicht.html')

def koerperschaftstypen_add(request):

    print(request.method)
    if request.method == 'GET':
        form = KoerperschaftstypenForm()
        return render(request, 'orga/koerperschaftstypen/koerperschaftstypen_uebersicht.html#koerperschaftstypen_add_form', {'form': form})
    
    if request.method == 'POST':
        form = KoerperschaftstypenForm(request.POST)

        if form.is_valid():
            print("form is valid")
            ktyp = form.save()
            if request.headers.get('HX-Request'):
                return render(request, 'orga/koerperschaftstypen/koerperschaftstypen_uebersicht.html#koerperschaftstypen_row', {'ktyp': ktyp})
            return redirect('koerperschaftstypenuebersicht')
        else:
            print("form is not valid")
            return HttpResponse('alles doof gelaufen')

    return render(request, 'orga/koerperschaftstypen/koerperschaftstypen_uebersicht.html')

def koerperschaftstypen_edit(request, id):
    return render(request, 'orga/koerperschaftstypen/koerperschaftstypen_uebersicht.html#koerperschaftstypen_edit_form', {'id': id})

def koerperschaftstypen_delete(request, id):
    return render(request, 'orga/koerperschaftstypen/koerperschaftstypen_uebersicht.html#koerperschaftstypen_delete_form', {'id': id})



# CRUD GEMEINDEN

def gemeindenuebersicht(request):

    gemeinden = Gemeinden.objects.all().order_by('gemeindenummer')
    
    return render(request, 'orga/gemeinde/gemeindeuebersicht.html', {'gemeinden': gemeinden})

def gemeinde_add(request):
    if request.method == 'GET':
        form = GemeindenForm()
        return render(request, 'orga/gemeinde/gemeindeuebersicht.html#gdetable_add', {'form': form})
    
    if request.method == 'POST':
        form = GemeindenForm(request.POST)

        if form.is_valid():
            print("form is valid")
            gde = form.save()
            if request.headers.get('HX-Request'):
                return render(request, 'orga/gemeinde/gemeindeuebersicht.html#gdetablerow', {'gemeinde': gde})
            return redirect('gemeindenuebersicht')
        else:
            print("form is not valid")
            return HttpResponse('alles doof gelaufen')

    return render(request, 'orga/gemeindeuebersicht.html#gdetable_add')

def gemeinde_edit(request, id):
    
    gde = get_object_or_404(Gemeinden, id=id)
    
    if request.method == 'POST':
        print("post request received")
        form = GemeindenForm(request.POST, instance=gde)

        if form.is_valid():
            print("form is valid")
            gde = form.save()
            if request.headers.get('HX-Request'):
                return render(request, 'orga/gemeinde/gemeindeuebersicht.html#gdetablerow', {'gemeinde': gde})
            return redirect('gemeindenuebersicht')
        else:
           
            return HttpResponse('alles doof gelaufen')
    else:
        form = GemeindenForm(instance=gde)
    
    return render(request, 'orga/gemeinde/gemeindeuebersicht.html#gdetable_edit', {'gemeinde': gde, 'form': form})

def gemeinde_delete(request, id):
    return render(request, 'orga/gemeinde/gemeinde_delete.html', {'id': id})



# CRUD OrgGliederungstiefe

def orggliederungstiefe_uebersicht(request):
    return render(request, 'orga/orggliederungstiefe_uebersicht.html')

def orggliederungstiefe_add(request):
    return render(request, 'orga/orggliederungstiefe_add.html')

def orggliederungstiefe_edit(request, id):
    return render(request, 'orga/orggliederungstiefe_edit.html', {'id': id})

def orggliederungstiefe_delete(request, id):
    return render(request, 'orga/orggliederungstiefe_delete.html', {'id': id})

# CRUD Organsationseinheiten

def organisationseinheiten_uebersicht(request):
    return render(request, 'orga/organisationseinheiten_uebersicht.html')

def organisationseinheiten_add(request):
    return render(request, 'orga/organisationseinheiten_add.html')

def organisationseinheiten_edit(request, id):
    return render(request, 'orga/organisationseinheiten_edit.html', {'id': id})

def organisationseinheiten_delete(request, id):
    return render(request, 'orga/organisationseinheiten_delete.html', {'id': id})

#CRUD AUfgaben 

def aufgaben_uebersicht(request):
    return render(request, 'orga/aufgaben_uebersicht.html')

def aufgaben_add(request):
    return render(request, 'orga/aufgaben_add.html')

def aufgaben_edit(request, id):
    return render(request, 'orga/aufgaben_edit.html', {'id': id})

def aufgaben_delete(request, id):
    return render(request, 'orga/aufgaben_delete.html', {'id': id})

# CRUD GVP

def gvp_uebersicht(request):
    return render(request, 'orga/gvp_uebersicht.html')

def gvp_add(request):
    return render(request, 'orga/gvp_add.html')

def gvp_edit(request, id):
    return render(request, 'orga/gvp_edit.html', {'id': id})

def gvp_delete(request, id):
    return render(request, 'orga/gvp_delete.html', {'id': id})

# CRUD Taetigkeiten Organisationseinheiten model = TaetigkeitenOrg

def taetigkeitenorg_uebersicht(request):
    return render(request, 'orga/taetigkeitenorg_uebersicht.html')

def taetigkeitenorg_add(request):
    return render(request, 'orga/taetigkeitenorg_add.html')

def taetigkeitenorg_edit(request, id):
    return render(request, 'orga/taetigkeitenorg_edit.html', {'id': id})

def taetigkeitenorg_delete(request, id):
    return render(request, 'orga/taetigkeitenorg_delete.html', {'id': id})





