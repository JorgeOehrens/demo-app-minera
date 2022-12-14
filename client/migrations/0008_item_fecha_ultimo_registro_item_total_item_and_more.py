# Generated by Django 4.0.4 on 2022-04-22 06:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_entrada_fecha_registro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='fecha_ultimo_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 22, 2, 22, 11, 529454), null=None),
        ),
        migrations.AddField(
            model_name='item',
            name='total_item',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 22, 2, 22, 11, 529454), null=None),
        ),
        migrations.AlterField(
            model_name='salida',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 22, 2, 22, 11, 529454), null=None),
        ),
    ]
