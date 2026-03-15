from django.db import models

from orga.models import Gemeinden

class Defaultwerte(models.Model):
    """Systemweite Standardwerte (z.B. aktuelles Haushaltsjahr)."""
    def_jahr = models.IntegerField(verbose_name="Standard-Haushaltsjahr")
    def_hh = models.CharField(max_length=50, null=True, blank=True,
                               verbose_name="Standard-Haushalt")
    def_gem = models.ForeignKey(
        Gemeinden, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="Standard-Gemeinde"
    )

    class Meta:
        db_table = 'Defaultwerte'
        verbose_name = 'Defaultwert'

    def __str__(self):
        return f"Defaultjahr: {self.def_jahr}, Gemeinde: {self.def_gem}"