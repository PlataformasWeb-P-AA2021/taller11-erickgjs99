from django.contrib import admin

# Register your models here.
from administrativo.models import Edificio, Departamento
from import_export.admin import ImportExportModelAdmin


class EdificioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion')


admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('nombreProp', 'costo', 'numCuartos', 'edificio')
    search_fields = ('nombreProp', 'edificio')

admin.site.register(Departamento, DepartamentoAdmin)