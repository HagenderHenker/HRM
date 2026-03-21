
from django import forms
from .models import Stellenarten, Haushalte, Teilhaushalte, Produkte, Kostenstellen


# Standard-Formulare für die CRUD-Operationen der Modelle in stellenplan/models.py

class StellenartenForm(forms.ModelForm):
    class Meta:
        model = Stellenarten
        fields = '__all__'

class HaushalteForm(forms.ModelForm):
    class Meta:
        model = Haushalte
        fields = '__all__'

class TeilhaushalteForm(forms.ModelForm):
    class Meta:
        model = Teilhaushalte
        fields = '__all__'

class ProdukteForm(forms.ModelForm):
    class Meta:
        model = Produkte
        fields = '__all__'

class KostenstellenForm(forms.ModelForm):
    class Meta:
        model = Kostenstellen
        fields = '__all__'

