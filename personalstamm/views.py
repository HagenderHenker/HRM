from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.

def personaluebersicht(request):
    return HttpResponse("Personalübersicht")
