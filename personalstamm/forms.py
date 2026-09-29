from django import forms
from . models import VergGrp, StundenVZAE, Tabellenentgelt, Beurteilungstypen, PersFortschritt, Kinder, AusWeiterbildung, Beurteilungen, Pruefungen, TaetigkeitenPersonal, PersSonst, Personalstamm

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
        fields = ['ab_datum', 'bis_datum', 'eingruppierung', 'stufe', 'entgelt', 'kinderzuschlag', 'sonstige_zulagen', 'vwl_ag', 'gesamt_brutto', 'entgeltumwandlung', 'entgeltumwandlung_text', 'ag_sv', 'ag_zvk', 'ag_sonstiges', 'ag_sonstiges_text', 'bemerkungen']

class KinderForm(forms.ModelForm):
    class Meta:
        model = Kinder
        fields =['name_kind', 'geburtsdatum', 'kinderstatus']

class AusWeiterbildungForm(forms.ModelForm):
    class Meta:
        model = AusWeiterbildung
        fields = ['ausbildungsziel', 'ausbildung_bei', 'von', 'bis', 'bemerkungen']

class BeurteilungenForm(forms.ModelForm):
    class Meta:
        model = Beurteilungen
        fields = ['datum', 'beurteilung_von', 'beurteilung_bis', 'beurteilungstyp', 'note', 'beurteilender', 'bemerkungen']


class PruefungenForm(forms.ModelForm):
    class Meta:
        model = Pruefungen
        fields = ['bezeichnung', 'ort', 'abgenommen_durch', 'datum', 'ergebnis',
                  'wiederholungspruefung', 'lehrgangszuschuss', 'bemerkungen_lehrgangszusch', 'zeugnis']
    
class TaetigkeitenPersonalForm(forms.ModelForm):
    class Meta:
        model = TaetigkeitenPersonal
        fields = fields = ['oeffentlicher_dienst', 'arbeitgeber', 'beginn_der_taet', 'ende_der_taet', 'art_des_dv', 'aufgabengebiet']

class PersSonstForm(forms.ModelForm):
    class Meta:
        model = PersSonst
        fields = ['sonstiges', 'zeitraum']

class PersonalstammForm(forms.ModelForm):
    class Meta:
        model = Personalstamm
        fields = '__all__'

class PersonalstammForm_shortened(forms.ModelForm):

    class Meta:
        model = Personalstamm
        fields = ['pers_nr', 'nachname', 'vorname', 'geburtsdatum', 'gemeinde', 'einsatzort']
