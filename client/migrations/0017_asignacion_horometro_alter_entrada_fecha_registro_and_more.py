# Generated by Django 4.0.4 on 2022-05-06 00:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0016_registro_stock_horometro_imagen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacion',
            name='horometro',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 5, 5, 20, 56, 13, 366500), null=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='fecha_ultimo_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 5, 5, 20, 56, 13, 366500), null=None),
        ),
        migrations.AlterField(
            model_name='registro_stock',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 5, 5, 20, 56, 13, 366500), null=None),
        ),
        migrations.AlterField(
            model_name='salida',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 5, 5, 20, 56, 13, 366500), null=None),
        ),
    ]