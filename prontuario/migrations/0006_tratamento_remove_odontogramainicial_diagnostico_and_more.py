# Generated by Django 4.0.3 on 2022-11-22 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prontuario', '0005_alter_dente_doenca_alter_dente_procedimento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tratamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, choices=[('canal', 'Canal'), ('limpeza', 'limpeza'), ('remoção de tartaro', 'remoção de tartaro'), ('aplicacao de fluor', 'aplicacao de fluor'), ('nenhum', 'nenhum')], default='nenhum', max_length=100, verbose_name='procedimento')),
            ],
            options={
                'verbose_name_plural': 'Tratamentos',
            },
        ),
        migrations.RemoveField(
            model_name='odontogramainicial',
            name='diagnostico',
        ),
        migrations.RemoveField(
            model_name='odontogramainicial',
            name='prontuario',
        ),
        migrations.RemoveField(
            model_name='dente',
            name='procedimento',
        ),
        migrations.RemoveField(
            model_name='odontograma',
            name='odontograma_inicial',
        ),
        migrations.AddField(
            model_name='odontograma',
            name='dente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='odontograma_dente', to='prontuario.dente'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='dente',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='atendimento_dente', to='prontuario.dente'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='prontuario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='atendimento_prontuario', to='prontuario.prontuario'),
        ),
        migrations.AlterField(
            model_name='dente',
            name='doenca',
            field=models.ManyToManyField(blank=True, related_name='dente_doencas', to='prontuario.doenca'),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='nome',
            field=models.TextField(blank=True, choices=[('carie', 'Carie'), ('cáries', 'cáries'), ('gengivite', 'gengivite'), ('tártaro', 'tártaro'), ('infecções', 'infecções'), ('sensibilidade', 'sensibilidade'), ('nenhuma', 'nenhuma')], default='nenhuma', verbose_name='Doença'),
        ),
        migrations.AlterField(
            model_name='odontograma',
            name='prontuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='odontograma_prontuario', to='prontuario.prontuario'),
        ),
        migrations.DeleteModel(
            name='Diagnostico',
        ),
        migrations.DeleteModel(
            name='OdontogramaInicial',
        ),
        migrations.DeleteModel(
            name='Procedimento',
        ),
        migrations.AddField(
            model_name='dente',
            name='tratamento',
            field=models.ManyToManyField(blank=True, related_name='dente_tratamentos', to='prontuario.tratamento'),
        ),
    ]
