from django import template
from client.models import Item, Registro_stock
import datetime

register = template.Library()
@register.simple_tag
def ingresos(nombre_item):
    item_id=Item.objects.get(nombre=nombre_item)
    item_id=item_id.id

    registros_item=Registro_stock.objects.filter(item=item_id)
    registros_item=registros_item.filter(movimiento="Ingreso")

    fecha_actual=datetime.datetime.now()
    fecha= fecha_actual +datetime.timedelta(days=1)    
    
    año=str(fecha.year)
    mes=str(fecha.month)
    dia=str(fecha.day)


    a= fecha_actual -datetime.timedelta(days=8)    
    año_a=str(a.year)
    mes_a=str(a.month)
    dia_a=str(a.day)
    fecha_semana=año_a + "-" + mes_a + "-" + dia_a
    fecha_hoy=año + "-" + mes + "-" + dia
    print(fecha_semana, ' - ',fecha)


    registros_item_fecha=registros_item.filter(fecha__range=[fecha_semana, fecha_hoy])

    n_registros_item_fecha=registros_item_fecha.count()

    return (n_registros_item_fecha)


register.filter('ingresos', ingresos)


@register.simple_tag
def salidas(nombre_item):
    item_id=Item.objects.get(nombre=nombre_item)
    item_id=item_id.id

    registros_item=Registro_stock.objects.filter(item=item_id)
    registros_item=registros_item.filter(movimiento="Salida")

    fecha_actual=datetime.datetime.now()
    fecha= fecha_actual +datetime.timedelta(days=1)    
    año=str(fecha.year)
    mes=str(fecha.month)
    dia=str(fecha.day)


    a= fecha_actual -datetime.timedelta(days=7)    
    año_a=str(a.year)
    mes_a=str(a.month)
    dia_a=str(a.day)
    fecha_semana=año_a + "-" + mes_a + "-" + dia_a
    fecha_hoy=año + "-" + mes + "-" + dia


    registros_item_fecha=registros_item.filter(fecha__range=[fecha_semana, fecha_hoy])

    n_registros_item_fecha=registros_item_fecha.count()

    return (n_registros_item_fecha)


register.filter('salidas', salidas)
