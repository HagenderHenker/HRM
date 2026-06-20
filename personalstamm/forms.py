from django import forms
from . models import VergGrp, StundenVZAE, Tabellenentgelt, Beurteilungstypen, PersFortschritt, Kinder, AusWeiterbildung, Beurteilungen, Pruefungen, TaetigkeitenPersonal, PersSonst

class VergGrpForm(forms.ModelForm):

    class Meta:
        model = VergGrp
        fields = '__all__'


class StundenVZAEForm(forms.ModelForm):
    class Meta:
        model = StundenVZAE
        fields = '__all__'

class TabellenentgeltForm(forms.ModelForm):
    class Meta:
        model = Tabellenentgelt
        fields = '__all__'

class BeurteilungstypenForm(forms.ModelForm):
    class Meta:
        model = Beurteilungstypen
        fields = '__all__'

class PersFortschrittForm(forms.ModelForm):
    class Meta:
        model = PersFortschritt
        fields = '__all__'

class KinderForm(forms.ModelForm):
    class Meta:
        model = Kinder
        fields = '__all__'

class AusWeiterbildungForm(forms.ModelForm):
    class Meta:
        model = AusWeiterbildung
        fields = '__all__'

class BeurteilungenForm(forms.ModelForm):
    class Meta:
        model = Beurteilungen
        fields = '__all__'

class PruefungenForm(forms.ModelForm):
    class Meta:
        model = Pruefungen
        fields = '__all__'
    
class TaetigkeitenPersonalForm(forms.ModelForm):
    class Meta:
        model = TaetigkeitenPersonal
        fields = '__all__'

class PersSonstForm(forms.ModelForm):
    class Meta:
        model = PersSonst
        fields = '__all__'

