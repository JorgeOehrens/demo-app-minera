# Generated by Django 4.0.4 on 2022-05-31 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0026_alter_entrada_fecha_registro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_stock',
            name='horometro_imagen2',
            field=models.FileField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 5, 31, 12, 4, 31, 81730), null=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='fecha_ultimo_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 5, 31, 12, 4, 31, 80731), null=None),
        ),
        migrations.AlterField(
            model_name='registro_stock',
            name='fecha',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 5, 31, 12, 4, 31, 82727), null=None),
        ),
        migrations.AlterField(
            model_name='registro_stock',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 5, 31, 12, 4, 31, 82727), null=None),
        ),
        migrations.AlterField(
            model_name='salida',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 5, 31, 12, 4, 31, 81730), null=None),
        ),
    ]