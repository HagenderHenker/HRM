from django.shortcuts import render


# Create your views here.

# CRUD GEMEINDEN

def gemeindenuebersicht(request):
    return render(request, 'orga/gemeindeuebersicht.html')

def gemeinde_add(request):
    return render(request, 'orga/gemeinde_add.html')

def gemeinde_edit(request, id):
    return render(request, 'orga/gemeinde_edit.html', {'id': id})

def gemeinde_delete(request, id):
    return render(request, 'orga/gemeinde_delete.html', {'id': id})

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





