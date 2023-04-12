# Generated by Django 4.0.3 on 2023-02-06 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prontuario', '0006_tratamento_remove_odontogramainicial_diagnostico_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estenografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(blank=True, choices=[('carie', 'Carie'), ('cáries', 'cáries'), ('gengivite', 'gengivite'), ('tártaro', 'tártaro'), ('infecções', 'infecções'), ('sensibilidade', 'sensibilidade'), ('nenhuma', 'nenhuma')], default='nenhuma', max_length=25, verbose_name='nome')),
            ],
            options={
                'verbose_name_plural': 'Doenças',
            },
        ),
        migrations.RemoveField(
            model_name='dente',
            name='doenca',
        ),
        migrations.RemoveField(
            model_name='dente',
            name='tratamento',
        ),
        migrations.AlterField(
            model_name='dente',
            name='prontuario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='dente_prontuario', to='prontuario.prontuario'),
        ),
        migrations.DeleteModel(
            name='Doenca',
        ),
        migrations.AddField(
            model_name='dente',
            name='distal',
            field=models.ManyToManyField(blank=True, related_name='dente_distal', to='prontuario.estenografia'),
        ),
        migrations.AddField(
            model_name='dente',
            name='lingual',
            field=models.ManyToManyField(blank=True, related_name='dente_lingual', to='prontuario.estenografia'),
        ),
        migrations.AddField(
            model_name='dente',
            name='mesial',
            field=models.ManyToManyField(blank=True, related_name='dente_mesial', to='prontuario.estenografia'),
        ),
        migrations.AddField(
            model_name='dente',
            name='oclusal',
            field=models.ManyToManyField(blank=True, related_name='dente_oclusal', to='prontuario.estenografia'),
        ),
        migrations.AddField(
            model_name='dente',
            name='vestibular',
            field=models.ManyToManyField(blank=True, related_name='dente_vestibular', to='prontuario.estenografia'),
        ),
    ]