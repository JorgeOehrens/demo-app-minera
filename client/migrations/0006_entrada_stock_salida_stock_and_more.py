# Generated by Django 4.0.4 on 2022-04-22 03:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_rename_fecha_entrada_fecha_entrada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='salida',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 21, 23, 55, 1, 579513), null=None),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='movimiento',
            field=models.CharField(choices=[('Ingreso', 'Ingreso'), ('Salida', 'Salida')], default='Movimiento no seleccionado', max_length=255),
        ),
        migrations.AlterField(
            model_name='salida',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 21, 23, 55, 1, 579513), null=None),
        ),
    ]