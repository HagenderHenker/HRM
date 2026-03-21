from django.db import models
from treebeard.mp_tree import MP_Node
#from stellenplan.models import Teilhaushalte, Stellenplan

# Referenz- und Lookup-Tabellen

class Gemeinden(models.Model):
    """Mandantenfähigkeit – ermöglicht Verwaltung mehrerer Gemeinden."""
    gemeindenummer = models.IntegerField(unique=True, verbose_name="Gemeindenummer")
    gemeinde = models.CharField(max_length=255, verbose_name="Gemeindename")
    arbeitgebernummerPPA = models.CharField(max_length=50, null=True, blank=True, verbose_name="Arbeitgebernummer PPA")
    arbeitgebernummerZVK = models.CharField(max_length=50, null=True, blank=True, verbose_name="Arbeitgebernummer ZVK")
    arbeitgebernummerRV = models.CharField(max_length=50, null=True, blank=True, verbose_name="Arbeitgebernummer RV")
    aktiv = models.BooleanField(default=True, verbose_name="Aktiv")
    gueltig_bis = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Gültig bis")
    class Meta:
        db_table = 'Gemeinden'
        verbose_name = 'Gemeinde'
        verbose_name_plural = 'Gemeinden'

    def __str__(self):
        return self.gemeinde


class OrgGliederungstiefe(models.Model):
    """Definiert die Hierarchieebenen der Organisationsstruktur."""
    gliederungstiefe = models.IntegerField(verbose_name="Tiefenstufe")
    bezeichnung = models.CharField(max_length=255, verbose_name="Bezeichnung")

    class Meta:
        db_table = 'OrgGliederungstiefe'
        verbose_name = 'Org. Gliederungstiefe'

    def __str__(self):
        return f"{self.gliederungstiefe} – {self.bezeichnung}"
    
class Organisationseinheiten(MP_Node):
    """
    Organisationsstruktur der Gemeinde (Ämter, Abteilungen, Teams).
    Selbstreferenz über ueber_org für hierarchische Darstellung.
    """
    org = models.CharField(max_length=50, verbose_name="ORG-Kürzel", unique=True)
    organisationseinheit = models.CharField(max_length=255, verbose_name="Bezeichnung")
    gliederungstiefe = models.ForeignKey(OrgGliederungstiefe, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Gliederungstiefe")
    unterste = models.CharField(max_length=10, null=True, blank=True, verbose_name="Unterste Ebene (J/N)")
    ueber_org = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='untergeordnete', verbose_name="Übergeordnete OE")
    th_zuordnung = models.ManyToManyField('stellenplan.Teilhaushalte', null=True, blank=True, verbose_name="Teilhaushalt")
    neben = models.BooleanField(default=False, verbose_name="Nebenstelle")
    stab = models.BooleanField(default=False, verbose_name="Stabsstelle")
    gemeinde = models.ForeignKey(Gemeinden, on_delete=models.PROTECT, verbose_name="Gemeinde")
    jahr = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Gültig ab")
    aktiv = models.BooleanField(default=True, verbose_name="Aktiv")
    gueltig_bis = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Gültig bis")
    
    class Meta:
        db_table = 'Organisationseinheiten'
        verbose_name = 'Organisationseinheit'
        verbose_name_plural = 'Organisationseinheiten'

    def __str__(self):
        return f"{self.org} – {self.organisationseinheit}"
    

class Aufgaben(models.Model):
    """Aufgabenportfolio der Gemeinde (Aufgabenkatalog)."""

    AUFGABENPFLICHTTYPEN = [
        ('PflichtSV', 'Pflichtaufgabe der Selbstverwaltung'),
        ('FreiwilligSV', 'Freiwillige Aufgabe der Selbstverwaltung'),
        ('Auftrag', 'Auftragsangelegenheit'),
        ('Management', 'Managementaufgabe'),
        ('Sonstige', 'Sonstige Aufgabe'),
    ]
    aufg_gliederung = models.CharField(max_length=50, null=True, blank=True, verbose_name="Gliederungsnummer")
    errichtung = models.DateTimeField(null=True, blank=True, verbose_name="Aufgenommen am")
    aufgabe_bez = models.CharField(max_length=255, null=True, blank=True, verbose_name="Aufgabenbezeichnung")
    grundlage = models.CharField(max_length=255, null=True, blank=True, verbose_name="Rechtsgrundlage")
    aufg_beschreibung = models.CharField(max_length=500, null=True, blank=True, verbose_name="Beschreibung")
    aufgabentyp = models.CharField(max_length=100, null=True, blank=True, verbose_name="Aufgabentyp")
    aufgabenverpflichtung = models.CharField(max_length=50, choices=AUFGABENPFLICHTTYPEN, null=True, blank=True, verbose_name="Aufgabenverpflichtung")
    gv_zuordnung = models.IntegerField(null=True, blank=True, verbose_name="Geschäftsverteilung")
    verkn_vg = models.CharField(max_length=100, null=True, blank=True, verbose_name="Verknüpfte VG")
    
    class Meta:
        db_table = 'Aufgaben'
        verbose_name = 'Aufgabe'
        verbose_name_plural = 'Aufgaben'

    def __str__(self):
        return f"{self.aufg_gliederung} – {self.aufgabe_bez}"

class Geschaeftsverteilung(MP_Node):
    """Geschäftsverteilungsplan der Gemeinde."""
    gvid = models.IntegerField(verbose_name="GV-ID")
    gemeinde = models.ForeignKey(Gemeinden, on_delete=models.PROTECT, verbose_name="Gemeinde")
    haushaltsjahr = models.IntegerField(verbose_name="Haushaltsjahr")
    gesch_v_nr = models.CharField(max_length=50, null=True, blank=True, verbose_name="GV-Nummer")
    gv_bez = models.CharField(max_length=255, null=True, blank=True, verbose_name="GV-Bezeichnung")
    beschreibung_lang = models.TextField(null=True, blank=True, verbose_name="Ausführliche Beschreibung")
    produkt = models.CharField(max_length=50, null=True, blank=True, verbose_name="Produkt")
    org_einheit = models.ForeignKey(Organisationseinheiten, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Organisationseinheit")

    class Meta:
        db_table = 'Geschaeftsverteilung'
        verbose_name = 'Geschäftsverteilung'

    def __str__(self):
        return f"{self.gesch_v_nr} – {self.gv_bez}"


class TaetigkeitenORG(models.Model):
    """Tätigkeitskatalog der Organisation (Arbeitsplatzbeschreibung)."""
    taet_id = models.IntegerField(verbose_name="Tätigkeits-ID")
    taet_nr = models.CharField(max_length=50, null=True, blank=True, verbose_name="Tätigkeitsnummer")
    bezeichnung = models.CharField(max_length=255, null=True, blank=True, verbose_name="Bezeichnung")
    zuord_gvid = models.ForeignKey(Geschaeftsverteilung, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Zuordnung GV")
    fallzahl = models.IntegerField(null=True, blank=True, verbose_name="Fallzahl")
    bearbeitungszeit = models.CharField(max_length=50, null=True, blank=True, verbose_name="Bearbeitungszeit (min)")
    stelle_nr = models.ForeignKey('stellenplan.Stellenplan', on_delete=models.SET_NULL, null=True, blank=True,  verbose_name="Stelle")
    anteil_vzae = models.IntegerField(null=True, blank=True, verbose_name="Anteil VZAE (%)")

    class Meta:
        db_table = 'TaetigkeitenORG'
        verbose_name = 'Tätigkeit (ORG)'
        verbose_name_plural = 'Tätigkeiten (ORG)'

    def __str__(self):
        return f"{self.taet_nr} – {self.bezeichnung}"
