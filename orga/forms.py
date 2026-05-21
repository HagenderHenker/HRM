from django import forms
from .models import Gemeinden, Koerperschaftstypen, OrgGliederungstiefe, Organisationseinheiten, Aufgaben, Geschaeftsverteilung, TaetigkeitenORG


class KoerperschaftstypenForm(forms.ModelForm):
    class Meta:
        model = Koerperschaftstypen
        fields = '__all__'
    
    def clean_koerperschaftstyp(self):
        koerperschaftstyp = self.cleaned_data.get('koerperschaftstyp')
        if not koerperschaftstyp:
            raise forms.ValidationError("Der Körperschafstyp muss angegeben werden.")
        return koerperschaftstyp

class GemeindenForm(forms.ModelForm):
    class Meta:
        model = Gemeinden
        fields = '__all__'
    
    def clean_gemeinde(self):
        gemeinde = self.cleaned_data.get('gemeinde')
        if not gemeinde:
            raise forms.ValidationError("Die Gemeinde muss angegeben werden.")
        return gemeinde

    def clean_gemeindenummer(self):
        gemeindenummer = self.cleaned_data.get('gemeindenummer')
        # isdigit() gibt es nicht auf int → entfernen
        if gemeindenummer is None:
            raise forms.ValidationError("Pflichtfeld.")
        if not (1 <= gemeindenummer <= 100):
            raise forms.ValidationError("Muss zwischen 1 und 100 liegen.")
        return gemeindenummer
    
    