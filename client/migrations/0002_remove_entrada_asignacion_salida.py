# Generated by Django 4.0.4 on 2022-04-21 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='asignacion',
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('hora_registro', models.TimeField(blank=True, null=True)),
                ('unidad', models.IntegerField(default=0)),
                ('movimiento', models.CharField(choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')], default='Movimiento no seleccionado', max_length=255)),
                ('cantidad', models.IntegerField(default=0)),
                ('horometro', models.CharField(default='', max_length=255)),
                ('asignacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.asignacion')),
                ('creador_registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.item')),
            ],
        ),
    ]
