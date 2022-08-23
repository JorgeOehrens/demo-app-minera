
from django.urls.conf import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('stock' , views.avance, name="avance"),
    path('CrearPost' , views.CrearPost, name="CrearPost"),
    path('salida' , views.Salida2, name="salida"),
    path('CrearSalida' , views.CrearSalida, name="CrearSalida"),
    path('frentes-crear' , views.frentes_registro, name="frentes_registro"),




]