from django.db import models
from orga.models import Gemeinden

# Referenz- und Lookup-Tabellen
class VergGrp(models.Model):
    """Vergütungsgruppen / Besoldungsgruppen (TVöD / BeamtVG)."""
    verg_grp = models.CharField(max_length=50, verbose_name="Vergütungsgruppe", unique=True)
    bezeichnung = models.CharField(max_length=255, null=True, blank=True)
    beamter = models.BooleanField(default=False, verbose_name="Beamtenstelle")
    bo_an = models.CharField(max_length=50, null=True, blank=True,
                             verbose_name="Besoldungsordnung/Anlage")
    reihenfolge = models.IntegerField(null=True, blank=True, verbose_name="Reihenfolge")

    class Meta:
        db_table = 'VergGrp'
        verbose_name = 'Vergütungsgruppe'
        verbose_name_plural = 'Vergütungsgruppen'

    def __str__(self):
        return f"{self.verg_grp} – {self.bezeichnung}"
    
class StundenVZAE(models.Model):
    """Referenztabelle: Wochenstunden je Vollzeitäquivalent (VZAE)."""
    beamter = models.BooleanField(default=False)
    art = models.CharField(max_length=255, null=True, blank=True)
    urlaubstage = models.IntegerField(null=True, blank=True, verbose_name="Urlaubstage/Jahr")
    stunden = models.CharField(max_length=50, null=True, blank=True,
                               verbose_name="Wochenstunden")
    ab = models.DateField(verbose_name="Gültig ab", null=True, blank=True)
    bis = models.DateField(verbose_name="Gültig bis", null=True, blank=True)

    class Meta:
        db_table = 'StundenVZAE'
        verbose_name = 'Stunden/VZAE'

    def __str__(self):
        return f"{self.art} – {self.stunden}h"


class Tabellenentgelt(models.Model):
    """TVöD-Entgelttabelle mit Zeitreihe (gültig ab/bis)."""
    gilt_ab = models.DateField(verbose_name="Gültig ab")
    gilt_bis = models.DateField(null=True, blank=True, verbose_name="Gültig bis")
    verg_grp = models.ForeignKey(VergGrp, on_delete=models.PROTECT, verbose_name="Vergütungsgruppe")
    stufe = models.IntegerField(null=True, blank=True, verbose_name="Stufe")
    tabellenentgelt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                          verbose_name="Tabellenentgelt (ct)")

    class Meta:
        db_table = 'Tabellenentgelt'
        verbose_name = 'Tabellenentgelt'
        verbose_name_plural = 'Tabellenentgelte'

    def __str__(self):
        return f"{self.verg_grp} Stufe {self.stufe} ab {self.gilt_ab}"
    
class Beurteilungstypen(models.Model):
    """Referenztabelle für Beurteilungstypen (z.B. Leistungsbeurteilung, Befähigungsbeurteilung)."""
    typ = models.CharField(max_length=50, verbose_name="Beurteilungstyp")
    beschreibung = models.CharField(max_length=255, null=True, blank=True,
                                   verbose_name="Beschreibung")

    class Meta:
        db_table = 'Beurteilungstypen'
        verbose_name = 'Beurteilungstyp'
        verbose_name_plural = 'Beurteilungstypen'

    def __str__(self):
        return self.typ


# Personal Modelle
"""
class Personalstamm(models.Model):
    """
#    Enthält die Stammdaten der Mitarbeiter.
#    dazu gehören persönliche Informationen, Adressdaten, Eintritts- und Austrittsdaten sowie die Personalnummer.

"""
    personalnummer = models.CharField(max_length=20, unique=True)
    vorname = models.CharField(max_length=50)
    nachname = models.CharField(max_length=50)
    strasse = models.CharField(max_length=100)
    hausnummer = models.CharField(max_length=10)
    plz = models.CharField(max_length=10)
    ort = models.CharField(max_length=100)
    geburtsdatum = models.DateField()
    eintrittsdatum = models.DateField()
    austrittsdatum = models.DateField(null=True, blank=True)
    austrittsgrund = models.CharField(max_length=255, null=True, blank=True)
    
    

    def __str__(self):
        return f"{self.vorname} {self.nachname} ({self.personalnummer})"
"""
class Personalstamm(models.Model):
    """
    Stammdaten aller Mitarbeiter.
    Zentrale Tabelle des Personalmoduls.
    """
    pers_nr = models.IntegerField(unique=True, verbose_name="Personalnummer")
    nachname = models.CharField(max_length=255, verbose_name="Nachname")
    vorname = models.CharField(max_length=255, verbose_name="Vorname")
    strasse = models.CharField(max_length=255, null=True, blank=True, verbose_name="Straße/Hausnummer")
    ort = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ort")
    telefon = models.CharField(max_length=50, null=True, blank=True)
    mobil = models.CharField(max_length=50, null=True, blank=True)
    e_mail = models.EmailField(null=True, blank=True, verbose_name="E-Mail")
    gemeinde = models.ForeignKey(Gemeinden, on_delete=models.PROTECT, verbose_name="Gemeinde")
    einsatzort = models.CharField(max_length=255, null=True, blank=True, verbose_name="Einsatzort")

    # Familienstand (Zeitverlauf)
    verheiratet_seit = models.DateTimeField(null=True, blank=True, verbose_name="Verheiratet seit")
    verheiratet_mit = models.CharField(max_length=255, null=True, blank=True, verbose_name="Verheiratet mit")
    verwitwet_seit = models.DateTimeField(null=True, blank=True, verbose_name="Verwitwet seit")
    geschieden_seit = models.DateTimeField(null=True, blank=True, verbose_name="Geschieden seit")
    wiederverheiratet_seit = models.DateTimeField(null=True, blank=True, verbose_name="Wiederverheiratet seit")
    wiederverheiratet_mit = models.CharField(max_length=255, null=True, blank=True, verbose_name="Wiederverheiratet mit")

    # Dienstverhältnis
    eintritt = models.DateTimeField(null=True, blank=True, verbose_name="Eintrittsdatum")
    eintrittsgrund = models.CharField(max_length=255, null=True, blank=True, verbose_name="Eintrittsgrund")
    austritt = models.DateTimeField(null=True, blank=True, verbose_name="Austrittsdatum")
    austrittsgrund = models.CharField(max_length=255, null=True, blank=True, verbose_name="Austrittsgrund")
    beamter = models.BooleanField(default=False, verbose_name="Beamter")
    bda = models.DateTimeField(null=True, blank=True, verbose_name="Beamtendienstalter")
    sonstige = models.CharField(max_length=500, null=True, blank=True, verbose_name="Sonstige Angaben")

    # Wehrdienst
    wehrdienst_von = models.DateTimeField(null=True, blank=True, verbose_name="Wehrdienst von")
    wehrdienst_bis = models.DateTimeField(null=True, blank=True, verbose_name="Wehrdienst bis")

    # Schwerbehinderung
    gdb = models.IntegerField(null=True, blank=True, verbose_name="Grad der Behinderung (%)")
    behinderung = models.CharField(max_length=255, null=True, blank=True, verbose_name="Art der Behinderung")
    beh_ausweis_vom = models.DateTimeField(null=True, blank=True, verbose_name="Ausweis ausgestellt am")
    beh_ausweis_vorlagedatum = models.DateTimeField(null=True, blank=True, verbose_name="Ausweis vorgelegt am")
    beh_ausweis_gueltig_bis = models.DateTimeField(null=True, blank=True, verbose_name="Ausweis gültig bis")

    class Meta:
        db_table = 'Personalstamm'
        verbose_name = 'Mitarbeiter'
        verbose_name_plural = 'Personalstamm'

    def __str__(self):
        return f"{self.pers_nr} – {self.nachname}, {self.vorname}"

class PersFortschritt(models.Model):
    """
    Vergütungsentwicklung im Zeitablauf (Stufenaufstiege TVöD / Beförderungen).
    """
    pers_nr = models.ForeignKey(
        Personalstamm, on_delete=models.CASCADE,
        to_field='pers_nr', verbose_name="Mitarbeiter"
    )
    ab_datum = models.DateTimeField(verbose_name="Gültig ab")
    bis_datum = models.DateTimeField(null=True, blank=True, verbose_name="Gültig bis")
    verguetung = models.CharField(max_length=50, null=True, blank=True,
                                   verbose_name="Vergütungsgruppe")
    stufe = models.IntegerField(null=True, blank=True, verbose_name="Stufe")

    class Meta:
        db_table = 'PersFortschritt'
        verbose_name = 'Vergütungsfortschritt'
        verbose_name_plural = 'Vergütungsfortschritt'

    def __str__(self):
        return f"{self.pers_nr} – {self.verguetung} Stufe {self.stufe} ab {self.ab_datum}"

class Kinder(models.Model):
    """Kinder des Mitarbeiters (relevant für Kindergeld, Familienstand)."""
    pers_nr = models.ForeignKey(
        Personalstamm, on_delete=models.CASCADE,
        to_field='pers_nr', verbose_name="Mitarbeiter"
    )
    name_kind = models.CharField(max_length=255, null=True, blank=True,
                                  verbose_name="Name des Kindes")
    geburtsdatum = models.DateTimeField(null=True, blank=True,
                                         verbose_name="Geburtsdatum")
    kinderstatus = models.CharField(max_length=100, null=True, blank=True,
                                     verbose_name="Status (ehelich/adoptiert/...)")

    class Meta:
        db_table = 'Kinder'
        verbose_name = 'Kind'
        verbose_name_plural = 'Kinder'

    def __str__(self):
        return f"{self.name_kind} (*{self.geburtsdatum})"


class AusWeiterbildung(models.Model):
    """Aus- und Weiterbildungsmaßnahmen je Mitarbeiter."""
    pers_nr = models.ForeignKey(
        Personalstamm, on_delete=models.CASCADE,
        to_field='pers_nr', verbose_name="Mitarbeiter"
    )
    ausbildungsziel = models.CharField(max_length=255, null=True, blank=True,
                                        verbose_name="Ausbildungsziel")
    ausbildung_bei = models.CharField(max_length=255, null=True, blank=True,
                                       verbose_name="Ausbildung bei")
    von = models.DateTimeField(null=True, blank=True, verbose_name="Von")
    bis = models.DateTimeField(null=True, blank=True, verbose_name="Bis")
    bemerkungen = models.CharField(max_length=500, null=True, blank=True,
                                    verbose_name="Bemerkungen")

    class Meta:
        db_table = 'AusWeiterbildung'
        verbose_name = 'Aus-/Weiterbildung'
        verbose_name_plural = 'Aus-/Weiterbildungen'

    def __str__(self):
        return f"{self.pers_nr} – {self.ausbildungsziel}"

class Beurteilungen(models.Model):
    """
    Dienstliche Beurteilungen im Zeitablauf.
    Enthält Leistungsbeurteilung (LB) und Befähigungsbeurteilung (BDB).
    """
    pers_nr = models.ForeignKey(
        Personalstamm, on_delete=models.CASCADE,
        to_field='pers_nr', verbose_name="Mitarbeiter"
    )
    datum = models.DateTimeField(verbose_name="Beurteilungsdatum")
    beurteilung_von = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Beurteilungszeitraum von")
    beurteilung_bis = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="Beurteilungszeitraum bis")
    beurteilungstyp = models.ForeignKey(Beurteilungstypen, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Beurteilungstyp (LB/BDB)")
    note = models.CharField(max_length=50, null=True, blank=True,
                            verbose_name="Note/Ergebnis")
    beurteilender = models.CharField(max_length=255, null=True, blank=True,
                                     verbose_name="Beurteilender Vorgesetzter")
    bemerkungen = models.CharField(max_length=500, null=True, blank=True,
                                    verbose_name="Bemerkungen")

    class Meta:
        db_table = 'Beurteilungen'
        verbose_name = 'Beurteilung'
        verbose_name_plural = 'Beurteilungen'

    def __str__(self):
        return f"{self.pers_nr} – {self.beurteilungstyp} am {self.datum}: {self.note}"
    

class Pruefungen(models.Model):
    """Prüfungen, Abschlüsse und Lehrgänge je Mitarbeiter."""
    pers_nr = models.ForeignKey(Personalstamm, on_delete=models.CASCADE, to_field='pers_nr', verbose_name="Mitarbeiter")
    bezeichnung = models.CharField(max_length=255, null=True, blank=True, verbose_name="Prüfungsbezeichnung")
    ort = models.CharField(max_length=255, null=True, blank=True, verbose_name="Prüfungsort")
    abgenommen_durch = models.CharField(max_length=255, null=True, blank=True, verbose_name="Abgenommen durch")
    datum = models.DateTimeField(null=True, blank=True, verbose_name="Prüfungsdatum")
    ergebnis = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ergebnis")
    wiederholungspruefung = models.BooleanField(default=False, verbose_name="Wiederholungsprüfung")
    lehrgangszuschuss = models.BooleanField(default=False, verbose_name="Lehrgangszuschuss gewährt")
    bemerkungen_lehrgangszusch = models.CharField(max_length=500, null=True, blank=True, verbose_name="Bemerkungen Zuschuss")
    zeugnis = models.FileField(upload_to='zeugnisse/', null=True, blank=True, verbose_name="Zeugnis/Urkunde (Datei)")

    class Meta:
        db_table = 'Pruefungen'
        verbose_name = 'Prüfung'
        verbose_name_plural = 'Prüfungen'

    def __str__(self):
        return f"{self.pers_nr} – {self.bezeichnung} ({self.datum})"

class TaetigkeitenPersonal(models.Model):
    """Frühere Tätigkeiten / Berufslaufbahn des Mitarbeiters."""
    pers_nr = models.ForeignKey(
        Personalstamm, on_delete=models.CASCADE,
        to_field='pers_nr', verbose_name="Mitarbeiter"
    )
    oeffentlicher_dienst = models.BooleanField(default=False,
                                                verbose_name="Öffentlicher Dienst")
    arbeitgeber = models.CharField(max_length=255, null=True, blank=True,
                                    verbose_name="Arbeitgeber")
    beginn_der_taet = models.DateTimeField(null=True, blank=True,
                                            verbose_name="Beginn der Tätigkeit")
    ende_der_taet = models.DateTimeField(null=True, blank=True,
                                          verbose_name="Ende der Tätigkeit")
    art_des_dv = models.CharField(max_length=100, null=True, blank=True,
                                   verbose_name="Art des Dienstverhältnisses")
    aufgabengebiet = models.CharField(max_length=255, null=True, blank=True,
                                       verbose_name="Aufgabengebiet")

    class Meta:
        db_table = 'TaetigkeitenPersonal'
        verbose_name = 'Frühere Tätigkeit'
        verbose_name_plural = 'Frühere Tätigkeiten'

    def __str__(self):
        return f"{self.pers_nr} – {self.arbeitgeber}"


class PersSonst(models.Model):
    """Sonstige Personalangaben (z.B. Besonderheiten, Vermerke)."""
    pers_nr = models.ForeignKey(
        Personalstamm, on_delete=models.CASCADE,
        to_field='pers_nr', verbose_name="Mitarbeiter"
    )
    sonstiges = models.CharField(max_length=500, null=True, blank=True,
                                  verbose_name="Sonstiges")
    zeitraum = models.CharField(max_length=100, null=True, blank=True,
                                 verbose_name="Zeitraum")

    class Meta:
        db_table = 'PersSonst'
        verbose_name = 'Sonstige Personalangabe'
