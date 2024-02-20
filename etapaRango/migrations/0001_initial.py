# Generated by Django 4.2.9 on 2024-02-20 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('etapa', '0002_rename_nombre_estapa_etapa_nombre_etapa'),
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtapaRango',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tot_ganadores', models.IntegerField(blank=True, null=True)),
                ('id_etapa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='etapa.etapa')),
                ('id_rango', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rango.rango')),
            ],
        ),
    ]