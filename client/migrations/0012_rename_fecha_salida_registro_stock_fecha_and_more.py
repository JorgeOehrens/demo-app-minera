# Generated by Django 4.0.4 on 2022-04-27 03:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_alter_entrada_fecha_registro_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro_stock',
            old_name='fecha_salida',
            new_name='fecha',
        ),
        migrations.AlterField(
            model_name='entrada',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 26, 23, 31, 2, 567691), null=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='fecha_ultimo_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 26, 23, 31, 2, 567691), null=None),
        ),
        migrations.AlterField(
            model_name='registro_stock',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 26, 23, 31, 2, 568688), null=None),
        ),
        migrations.AlterField(
            model_name='salida',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 26, 23, 31, 2, 568688), null=None),
        ),
    ]
