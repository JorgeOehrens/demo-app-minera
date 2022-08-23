from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models.fields import DateField
from django.db.models.base import Model
from datetime import datetime
# Create your models here.

class Item(models.Model):

    creador_registro = models.ForeignKey(to=User, on_delete=models.CASCADE)
    nombre = models.CharField(default='No inscrito el nombre ', max_length=255)
    total_item = models.IntegerField(default=0)
    fecha_ultimo_registro=models.DateTimeField(default=datetime.now(), blank=None, null=None)
    unidad=models.CharField(default='Unidad', max_length=255)


    def __str__(self):
        return str(self.nombre)

class Asignacion(models.Model):

    creador_registro = models.ForeignKey(to=User, on_delete=models.CASCADE)
    nombre = models.CharField(default='No inscrito el nombre ', max_length=255)
    horometro = models.FloatField(default=0.0)


    def __str__(self):
        return str(self.nombre)

class Frente(models.Model):

    nombre = models.CharField(default='x', max_length=255)


    def __str__(self):
        return str(self.nombre)


class Entrada(models.Model):

    MOVIMIENTO =[
        ('Ingreso', 'Ingreso'),
        ('Salida', 'Salida'),
    ]

    creador_registro = models.ForeignKey(to=User, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(default=datetime.now(), blank=None, null=None)
    item=models.ForeignKey(to=Item, on_delete=models.CASCADE)
    fecha_entrada = models.DateTimeField()


    unidad=models.IntegerField(default=0)
    movimiento = models.CharField(default='Movimiento no seleccionado',choices=MOVIMIENTO , max_length=255)
    cantidad=models.IntegerField(default=0)
    horometro = models.CharField(default='x', max_length=255)
    stock=models.IntegerField(default=0)



    




    def __str__(self):
        return str(self.creador_registro) + " Entrada de " + str(self.item) + " Cantidad " + str(self.cantidad) 

class Salida(models.Model):

    MOVIMIENTO =[
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida'),
    ]




    fecha_registro = models.DateTimeField(default=datetime.now(), blank=None, null=None)

    creador_registro = models.ForeignKey(to=User, on_delete=models.CASCADE)
    fecha_salida = models.DateTimeField()
    item=models.ForeignKey(to=Item, on_delete=models.CASCADE)

    movimiento = models.CharField(default='Movimiento no seleccionado',choices=MOVIMIENTO , max_length=255)
    cantidad=models.IntegerField(default=0)
    horometro = models.FloatField(default=0.0)

    horometro_imagen = models.ImageField(upload_to='Horometro/%Y/%m/%d', null=False, blank=False , default='Horometro/blank.png')



    stock=models.IntegerField(default=0)
    

    asignacion=models.ForeignKey(to=Asignacion, on_delete=models.CASCADE)
    frente = models.ForeignKey(to=Frente, on_delete=models.CASCADE)





    def __str__(self):
        return str(self.creador_registro) + " Salida de " + str(self.item) + " Cantidad " + str(self.cantidad) 

class Registro_stock(models.Model):

    MOVIMIENTO =[
        ('Ingreso', 'Ingreso'),
        ('Salida', 'Salida'),
    ]




    fecha_registro = models.DateTimeField(default=datetime.now(), blank=None, null=None)

    creador_registro = models.ForeignKey(to=User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now(), blank=None, null=None)
    item=models.ForeignKey(to=Item, on_delete=models.CASCADE)

    movimiento = models.CharField(default='Movimiento no seleccionado',choices=MOVIMIENTO , max_length=255)
    cantidad=models.IntegerField(default=0)
    horometro = models.FloatField(default=0.0)
    stock=models.IntegerField(default=0)
    horometro_imagen =  models.ImageField(upload_to='Horometro/%Y/%m/%d', null=False, blank=False , default='Horometro/blank.png')
    horometro_imagen2 = models.FileField()
    imagen=models.IntegerField(default=0)

    asignacion=models.ForeignKey(to=Asignacion, on_delete=models.CASCADE)
    
    frente = models.ForeignKey(to=Frente, on_delete=models.CASCADE)




    def __str__(self):
        return str(self.movimiento)
