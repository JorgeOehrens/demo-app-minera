from django.contrib import admin
from .models import Entrada, Asignacion, Item, Salida,Frente , Registro_stock
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Entrada)
class EntradaAdmin(ImportExportModelAdmin):
    list_display = ('creador_registro','fecha_registro','item','fecha_entrada','unidad' , 'movimiento','cantidad','horometro','stock')


@admin.register(Asignacion)
class AsignacionAdmin(ImportExportModelAdmin):
    list_display = ('id','creador_registro','nombre','horometro')



@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    list_display = ('id','creador_registro','nombre','total_item','fecha_ultimo_registro', 'unidad')

@admin.register(Salida)
class SalidaAdmin(ImportExportModelAdmin):
    list_display = ('creador_registro','fecha_registro','item','fecha_salida' , 'movimiento','cantidad','horometro', 'horometro_imagen','asignacion','frente','stock')

@admin.register(Frente)
class FrenteAdmin(ImportExportModelAdmin):
    list_display = ('id','nombre', )


@admin.register(Registro_stock)
class Registro_stockAdmin(ImportExportModelAdmin):
    list_display = ('fecha_registro','creador_registro','fecha','item','movimiento','cantidad', 'horometro','stock','horometro_imagen','asignacion','frente')






