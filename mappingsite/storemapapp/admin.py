from django.contrib import admin
from storemapapp.models import Ruc


class RucAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Ruc', 'Domicilio', 'Departamento',
                    'Provincia', 'Distrito', 'Estado')

admin.site.register(Ruc, RucAdmin)

