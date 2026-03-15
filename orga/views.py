from django.shortcuts import render


# Create your views here.

# CRUD GEMEINDEN

def gemeindenuebersicht(request):
    return render(request, 'orga/gemeindenuebersicht.html')

def gemeinde_neu(request):
    return render(request, 'orga/gemeinde_neu.html')

def gemeinde_bearbeiten(request, id):
    return render(request, 'orga/gemeinde_bearbeiten.html', {'id': id})

def gemeinde_loeschen(request, id):
    return render(request, 'orga/gemeinde_loeschen.html', {'id': id})

# CRUD Organsationseinheiten



