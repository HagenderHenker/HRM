from django import forms
from .models import Gemeinden, OrgGliederungstiefe, Organisationseinheiten, Aufgaben, Geschaeftsverteilung, TaetigkeitenORG

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
        if gemeindenummer and not gemeindenummer.isdigit():
            raise forms.ValidationError("Die Gemeindennummer muss eine Zahl sein.")
        if gemeindenummer > 100 or gemeindenummer < 1:
            raise forms.ValidationError("Die Gemeindennummer muss zwischen 1 und 100 liegen.")
        return gemeindenummer
    
    