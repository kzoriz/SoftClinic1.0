# Generated by Django 4.0.3 on 2022-11-20 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prontuario', '0003_remove_atendimento_procedimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnostico',
            name='doenca',
        ),
    ]
