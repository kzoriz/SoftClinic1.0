# Generated by Django 4.0.3 on 2022-11-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prontuario', '0002_atendimento_dente_diagnostico_doenca_odontograma_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dente',
            name='procedimento',
        ),
        migrations.AddField(
            model_name='dente',
            name='procedimento',
            field=models.ManyToManyField(blank=True, related_name='dente', to='prontuario.procedimento'),
        ),
    ]