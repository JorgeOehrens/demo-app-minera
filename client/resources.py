from import_export import resources
from .models import Entrada, Asignacion, Item, Salida, Registro_stock


class EntradaResource(resources.ModelResource):
    class Meta:
        model = Entrada


class AsignacionResource(resources.ModelResource):
    class Meta:
        model = Asignacion

class ItemResource(resources.ModelResource):
    class Meta:
        model = Item

class SalidaResource(resources.ModelResource):
    class Meta:
        model = Salida

class Registro_stockResource(resources.ModelResource):
    class Meta:
        model = Registro_stock
