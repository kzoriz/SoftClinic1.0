# Generated by Django 4.0.3 on 2022-09-08 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0007_alter_paciente_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='data_nascimento',
            field=models.DateField(blank=True, verbose_name='Data de Nascimento'),
        ),
    ]