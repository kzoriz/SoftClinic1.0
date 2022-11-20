from django.db import models
from django.contrib.auth.models import User


class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="funcionario")
    imagem = models.ImageField(null=True, blank=True, default='padrao.png')
    #image = models.
    matricula = models.CharField(verbose_name="MatFunc", max_length=200, default="nenhuma")
    nome = models.CharField(verbose_name="Nome", max_length=200)
    telefone = models.CharField(verbose_name="Telefone", max_length=15)
    email = models.EmailField(verbose_name="Email", max_length=200)

    def __str__(self):
        return self.nome


class Docente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="docente")
    imagem = models.ImageField(null=True, blank=True, default='padrao.png')
    matricula = models.CharField(verbose_name="MatDocente", max_length=200)
    nome = models.CharField(verbose_name="Nome", max_length=200)
    telefone = models.CharField(verbose_name="Telefone", max_length=15)
    email = models.EmailField(verbose_name="Email", max_length=200)

    def __str__(self):
        return self.nome


class Discente(models.Model):

    PERIODO = [
        ('1', '1º'),
        ('2', '2º'),
        ('3', '3º'),
        ('4', '4º'),
        ('5', '5º'),
        ('6', '6º'),
        ('7', '7º'),
        ('8', '8º'),
        ('9', '9º'),
        ('10', '10º'),

    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="discente")
    imagem = models.ImageField(null=True, blank=True, default='padrao.png')
    matricula = models.CharField(verbose_name="MatDiscente", max_length=200)
    nome = models.CharField(verbose_name="Nome", max_length=200)
    periodo = models.CharField(verbose_name="Período", max_length=3)
    telefone = models.CharField(verbose_name="Telefone", max_length=15)
    email = models.EmailField(verbose_name="Email", max_length=200)

    def __str__(self):
        return self.nome

