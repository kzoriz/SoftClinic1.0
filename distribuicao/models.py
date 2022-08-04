from django.db import models
from usuarios.models import Docente


class Disciplina(models.Model):
    PERIODO = [
        ('1º', '1º'),
        ('2º', '2º'),
        ('3º', '3º'),
        ('4º', '4º'),
        ('5º', '5º'),
        ('6º', '6º'),
        ('7º', '7º'),
        ('8º', '8º'),
        ('9º', '9º'),
        ('10º', '10º'),

    ]

    nome = models.CharField(verbose_name="Nome Disciplina", max_length=200)
    codigo = models.CharField(verbose_name="CodDisc", max_length=200)
    periodo = models.CharField(verbose_name="Periodo", max_length=3, choices=PERIODO)

    def __str__(self):
        return self.nome