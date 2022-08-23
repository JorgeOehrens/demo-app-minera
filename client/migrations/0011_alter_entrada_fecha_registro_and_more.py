# Generated by Django 4.0.4 on 2022-04-27 03:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0010_alter_entrada_fecha_registro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 26, 23, 27, 52, 515297), null=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='fecha_ultimo_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 26, 23, 27, 52, 515297), null=None),
        ),
        migrations.AlterField(
            model_name='salida',
            name='fecha_registro',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 26, 23, 27, 52, 516294), null=None),
        ),
        migrations.CreateModel(
            name='Registro_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(blank=None, default=datetime.datetime(2022, 4, 26, 23, 27, 52, 516294), null=None)),
                ('fecha_salida', models.DateTimeField()),
                ('movimiento', models.CharField(choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')], default='Movimiento no seleccionado', max_length=255)),
                ('cantidad', models.IntegerField(default=0)),
                ('horometro', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('asignacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.asignacion')),
                ('creador_registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.item')),
            ],
        ),
    ]