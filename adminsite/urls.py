
from unicodedata import name
from django.urls.conf import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.home, name="home-admin"),
    path('stock', views.control_stock, name="control-stock"),
    path('stock/editar/<int:id>', views.edit_registro, name="edit_registro"),
    path('stock/eliminar/<int:id>', views.eliminar_registro, name="eliminar_registro"),

    path('registros', views.registros_total, name="registros"),
    path('actualizar_stock', views.actualizar_stock, name="actualizar_stock"),
    path('registro-fecha/<int:id>', views.registro_fecha, name="registro_fecha"),
    path('usuarios' , views.usuarios, name="usuarios"),
    path('usuarios/<int:id>', views.usuarios_details, name="usuarios_details"),

    path('export' , views.listresults, name="export"),
    path('registro' , views.registro, name="registro"),
    path('confirmar' , views.confirmar_contraseña, name="confirmar_contraseña"),

    
]