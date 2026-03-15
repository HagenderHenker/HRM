from django.db import models
from orga.models import Gemeinden, Organisationseinheiten
#from personalstamm.models import VergGrp, Personalstamm

# Referenz- und Lookup-Tabellen

class Stellenarten(models.Model):
    """Arten von Stellen (z.B. Vollzeit, Teilzeit, Beamtenstelle)."""
    stellenart = models.SmallIntegerField(verbose_name="Stellenart-Code")
    stellenart_bez = models.CharField(max_length=255, verbose_name="Bezeichnung")

    class Meta:
        db_table = 'Stellenarten'
        verbose_name = 'Stellenart'
        verbose_name_plural = 'Stellenarten'

    def __str__(self):
        return self.stellenart_bez
  
class Haushalte(models.Model):
    """Haushaltspläne je Gemeinde und Haushaltsjahr."""
    haushalt = models.CharField(max_length=50, verbose_name="Haushalts-Kürzel", unique=True)
    bezeichnung = models.CharField(max_length=255, verbose_name="Bezeichnung")
    haushaltsjahr = models.IntegerField(verbose_name="Haushaltsjahr")
    nachtrag = models.BooleanField(default=False, verbose_name="Nachtrag")
    verabschiedet = models.DateTimeField(null=True, blank=True, verbose_name="Verabschiedet am")
    genehmigt = models.DateTimeField(null=True, blank=True, verbose_name="Genehmigt am")
    planung_abgeschlossen = models.BooleanField(default=False, verbose_name="Planung abgeschlossen")
    gemeinde = models.ForeignKey(Gemeinden, on_delete=models.PROTECT, verbose_name="Gemeinde")
    arbeitstage = models.SmallIntegerField(null=True, blank=True, verbose_name="Arbeitstage/Jahr")

    class Meta:
        db_table = 'Haushalte'
        verbose_name = 'Haushalt'
        verbose_name_plural = 'Haushalte'

    def __str__(self):
        return f"{self.haushalt} ({self.haushaltsjahr})"


class Teilhaushalte(models.Model):
    """Teilhaushalte gemäß kommunalem Haushaltsrecht."""
    gemeinde = models.ForeignKey(Gemeinden, on_delete=models.PROTECT, verbose_name="Gemeinde")
    haushaltsjahr = models.IntegerField(verbose_name="Haushaltsjahr")
    th = models.CharField(max_length=50, verbose_name="TH-Kürzel")
    th_bezeichnung = models.CharField(max_length=255, verbose_name="Bezeichnung")

    class Meta:
        db_table = 'Teilhaushalte'
        verbose_name = 'Teilhaushalt'
        verbose_name_plural = 'Teilhaushalte'

    def __str__(self):
        return f"{self.th} – {self.th_bezeichnung}"

class Produkte(models.Model):
    """Produktplan der Gemeinde (NKF-Produktstruktur)."""
    gemeinde = models.ForeignKey(
        Gemeinden, on_delete=models.PROTECT, verbose_name="Gemeinde"
    )
    haushaltsjahr = models.IntegerField(verbose_name="Haushaltsjahr")
    produkt = models.IntegerField(null=True, blank=True, verbose_name="Produktnummer")
    bezeichnung = models.CharField(max_length=255, null=True, blank=True,
                                    verbose_name="Produktbezeichnung")
    teilhaushalt = models.ForeignKey(Teilhaushalte, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Teilhaushalt")

    class Meta:
        db_table = 'Produkte'
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkte'

    def __str__(self):
        return f"{self.produkt} – {self.bezeichnung}"

class Kostenstellen(models.Model):
    """
    Kostenstellenliste
    """
    kostenstelle = models.CharField(max_length=20, verbose_name="Kostenstelle", unique=True)
    bezeichnung = models.CharField(max_length=255, verbose_name="Bezeichnung")
    produktzuordnung = models.CharField(max_length=50, null=True, blank=True, verbose_name="Produktzuordnung")
    # Feld für Zuordnung zum Rechnungshofgutachten Personalbedarf der Verbandsgemeindeverwaltung bzw. zu anderen Gutachten
    zuordnungRechnungshof = models.CharField(max_length=50, null=True, blank=True, verbose_name="Zuordnung Rechnungshof")
    zuordnungGutachten = models.CharField(max_length=50, null=True, blank=True, verbose_name="Zuordnung Gutachten")
    stellenbemessungvom = models.DateTimeField(null=True, blank=True, verbose_name="Stellenbemessung vom")
    stellenbemessung = models.FileField(upload_to=None, max_length=100, null=True, blank=True, verbose_name="Stellenbemessung (z.B. Dokumentation der Berechnung)")

    class Meta:

        db_table = 'Kostenstellen'
        verbose_name = 'Kostenstelle'
        verbose_name_plural = 'Kostenstellen'

    def __str__(self):
        return f"{self.kostenstelle} – {self.bezeichnung}"  

#_________________________________________________________________________________________________________________________________
# S T E L L E N P L A N U N G
#_________________________________________________________________________________________________________________________________


class Stellenplan(models.Model):
    """
    Stellenplan gemäß §5 GemHVO RLP.
    Enthält die genehmigten Stellen je Haushaltsjahr.
    """
    haushaltsjahr = models.IntegerField(verbose_name="Haushaltsjahr")
    gemeinde = models.ForeignKey('orga.Gemeinden', on_delete=models.PROTECT, verbose_name="Gemeinde")
    stelle_nr = models.CharField(max_length=50, verbose_name="Stellennummer")
    stelle_nr_vj = models.CharField(max_length=50, null=True, blank=True, verbose_name="Stellennummer Vorjahr")
    bezeichnung = models.CharField(max_length=255, verbose_name="Stellenbezeichnung")
    einrichtungsdatum = models.DateTimeField(null=True, blank=True, verbose_name="Eingerichtet am")
    letzte_neubewertung = models.DateTimeField(null=True, blank=True, verbose_name="Letzte Neubewertung")
    stellenart = models.ForeignKey(Stellenarten, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Stellenart")
    verg_grp = models.ForeignKey('personalstamm.VergGrp', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Vergütungsgruppe")
    kw = models.BooleanField(default=False, verbose_name="Künftig wegfallend (kw)")
    ku = models.BooleanField(default=False, verbose_name="Künftig umzuwandeln (ku)")
    bemerkungen_druck = models.CharField(max_length=500, null=True, blank=True, verbose_name="Bemerkungen (Druck)")
    th = models.ForeignKey(Teilhaushalte, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Teilhaushalt")
    organisation = models.ForeignKey(Organisationseinheiten, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Organisationseinheit")
    stellenverweisung = models.CharField(max_length=255, null=True, blank=True, verbose_name="Stellenverweisung")
    bemerkungen_int = models.CharField(max_length=500, null=True, blank=True, verbose_name="Bemerkungen (intern)")
    produkt = models.IntegerField(null=True, blank=True, verbose_name="Produkt-ID")
    kostenstelle = models.ManyToManyField(Kostenstellen, null=True, blank=True, verbose_name="Kostenstelle")
    kostentraeger = models.CharField(max_length=50, null=True, blank=True, verbose_name="Kostenträger")
    plan = models.ForeignKey(Haushalte, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Haushaltsplan")

    class Meta:
        db_table = 'Stellenplan'
        verbose_name = 'Stelle'
        verbose_name_plural = 'Stellenplan'
        unique_together = [('haushaltsjahr', 'gemeinde', 'stelle_nr')]

    def __str__(self):
        return f"{self.stelle_nr} - {self.bezeichnung} - ({self.haushaltsjahr})"

class KostenstellenaufteilungStellen(models.Model):
    """
    Aufteilung der Stelle auf Kostenstellen (z.B. bei Teilzeitstellen).
    Zeitreihe der genehmigten Aufteilungen.
    """
    stelle = models.ForeignKey(Stellenplan, on_delete=models.CASCADE, verbose_name="Stelle")
    kostenstelle = models.ForeignKey(Kostenstellen, on_delete=models.CASCADE, verbose_name="Kostenstelle")
    aufteilung_prozent = models.FloatField(null=True, blank=True, verbose_name="Aufteilung (%)", default=100.0)
    gueltig_ab = models.DateTimeField(verbose_name="Gültig ab")
    gueltig_bis = models.DateTimeField(null=True, blank=True, verbose_name="Gültig bis")

    class Meta:
        db_table = 'KostenstellenaufteilungStellen'
        verbose_name = 'Kostenstellenaufteilung'
        verbose_name_plural = 'Kostenstellenaufteilungen'
        
    def __str__(self):
        return f"{self.stelle.stelle_nr} – {self.kostenstelle} ({self.gueltig_ab} bis {self.gueltig_bis})"

class StellenplanSoll(models.Model):
    """
    Soll-Werte im Stellenplan (Vollzeitäquivalente).
    Zeitreihe der genehmigten Stellenanteile.
    """
    buchungsdatum = models.DateField(verbose_name="Buchungsdatum", auto_now_add=False, auto_now=False)
    erfassungsdatum = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Erfassungsdatum")   
    stelle = models.ForeignKey(Stellenplan, on_delete=models.CASCADE, verbose_name="Stelle")
    #haushaltsjahr = models.IntegerField(verbose_name="Haushaltsjahr")
    #plan = models.CharField(max_length=50, null=True, blank=True, verbose_name="Plan-Variante")
    plan = models.ForeignKey(Haushalte, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Haushaltsplan")
    stellensoll_hhj = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Stellensoll HHJ (Anteile VZAE)")
    aend_stellensoll_hhj = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True, verbose_name="Änderung Stellensoll")
    aend_ab = models.DateTimeField(null=True, blank=True, verbose_name="Änderung gültig ab")
    ps_bemerkungen = models.CharField(max_length=500, null=True, blank=True, verbose_name="Bemerkungen")

    class Meta:
        db_table = 'StellenplanSoll'
        verbose_name = 'Stellenplan-Soll'

    def __str__(self):
        return f"{self.plan.gemeinde.gemeindenummer}-{self.plan.haushaltsjahr} | {self.stelle}: {self.stellensoll_hhj} VZAE"


class Stellenbesetzung(models.Model):
    """
    IST-Besetzung der Stellen durch Mitarbeiter.
    Verknüpft Personalstamm und Stellenplan – Herzstück des Soll-Ist-Vergleichs.
    """
    haushaltsjahr = models.IntegerField(verbose_name="Haushaltsjahr")
    stelle = models.ForeignKey(
        Stellenplan, on_delete=models.PROTECT, verbose_name="Stelle"
    )
    person = models.ForeignKey('personalstamm.Personalstamm', on_delete=models.PROTECT, verbose_name="Mitarbeiter")
    besetzungsart = models.IntegerField(null=True, blank=True, verbose_name="Besetzungsart")
    besetzung_ab = models.DateTimeField(null=True, blank=True, verbose_name="Besetzt ab")
    besetzung_bis = models.DateTimeField(null=True, blank=True, verbose_name="Besetzt bis")
    stunden = models.IntegerField(null=True, blank=True, verbose_name="Wochenstunden")

    class Meta:
        db_table = 'Stellenbesetzung'
        verbose_name = 'Stellenbesetzung'
        verbose_name_plural = 'Stellenbesetzungen'

    def __str__(self):
        return f"{self.stelle} → {self.person} ({self.haushaltsjahr})"
