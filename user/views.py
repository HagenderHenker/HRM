from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def useruebersicht(request):
    return HttpResponse("Userübersicht")