# Generated by Django 4.0.4 on 2022-04-21 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_remove_entrada_asignacion_salida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salida',
            name='unidad',
        ),
    ]
