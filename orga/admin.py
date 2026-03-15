

from django.contrib import admin
from .models import Gemeinden, OrgGliederungstiefe, Organisationseinheiten, Aufgaben, TaetigkeitenORG
admin.site.register(Gemeinden)
admin.site.register(OrgGliederungstiefe)
admin.site.register(Organisationseinheiten)
admin.site.register(Aufgaben)
admin.site.register(TaetigkeitenORG)


# Register your models here.

admin.site.site_header = "Stellenplanverwaltung - Admin"