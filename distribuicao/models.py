# from django.db import models
#
# from prontuario.models import Prontuario, Atendimento
# from usuarios.models import Docente, Discente
#
#
# class Disciplina(models.Model):
#     PERIODO = [
#         ('1º', '1º'),
#         ('2º', '2º'),
#         ('3º', '3º'),
#         ('4º', '4º'),
#         ('5º', '5º'),
#         ('6º', '6º'),
#         ('7º', '7º'),
#         ('8º', '8º'),
#         ('9º', '9º'),
#         ('10º', '10º'),
#
#     ]
#
#     nome = models.CharField(verbose_name="Nome Disciplina", max_length=200)
#     codigo = models.CharField(verbose_name="CodDisc", max_length=200)
#     periodo = models.CharField(verbose_name="Periodo", max_length=3, choices=PERIODO)
#
#     def __str__(self):
#         return self.nome
#
#
# class Agendamento(models.Model):
#     prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE, blank=True, related_name="agendamento")
#     atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE, blank=True, null=True, related_name="agendamento")
#     disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, blank=True, related_name="agendamento")
#     docente = models.ForeignKey(Docente, on_delete=models.CASCADE, blank=True, related_name="agendamento")
#     discente = models.ForeignKey(Discente, on_delete=models.CASCADE, blank=True, related_name="agendamento")
#     data_hora = models.DateTimeField(verbose_name="Data", blank=True)
#     done = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.prontuario.paciente.nome
#
#     class Meta:
#         verbose_name_plural = "Agendamentos"