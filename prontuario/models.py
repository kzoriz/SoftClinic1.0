from django.db import models
from pacientes.models import Paciente
from django.urls import reverse

SEXTANTE = [
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
]

PLACA_VISIVEL = [
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
]
CHOICES_RESULTADO = [
    ('Higiene Boa', 'Higiene Boa'),
    ('Higiene Regular', 'Higiene regular'),
    ('Higiene Ruim', 'Higiene Ruim'),
]

C_CHOICES = [
    ('SIM', 'SIM'),
    ('NAO', 'NÃO'),
]

ESTENOGRAFIA_CHOICES = [
    ('carie', 'Carie'),
    ('cáries', 'cáries'),
    ('gengivite', 'gengivite'),
    ('tártaro', 'tártaro'),
    ('infecções', 'infecções'),
    ('sensibilidade', 'sensibilidade'),
    ('nenhuma', 'nenhuma'),
]

TRATAMENTO_CHOICES = [
    ('canal', 'Canal'),
    ('limpeza', 'limpeza'),
    ('remoção de tartaro', 'remoção de tartaro'),
    ('aplicacao de fluor', 'aplicacao de fluor'),
    ('nenhum', 'nenhum'),
]

DENTE_CHOICES = [
    ('D11', 'D11'),
    ('D12', 'D12'),
    ('D13', 'D13'),
    ('D14', 'D14'),
    ('D15', 'D15'),
    ('D16', 'D16'),
    ('D17', 'D17'),
    ('D18', 'D18'),

    ('D21', 'D21'),
    ('D22', 'D23'),
    ('D23', 'D23'),
    ('D24', 'D24'),
    ('D25', 'D25'),
    ('D26', 'D26'),
    ('D27', 'D27'),
    ('D28', 'D28'),

    ('D31', 'D31'),
    ('D32', 'D32'),
    ('D33', 'D33'),
    ('D34', 'D34'),
    ('D35', 'D35'),
    ('D36', 'D36'),
    ('D37', 'D37'),
    ('D38', 'D38'),

    ('D41', 'D41'),
    ('D42', 'D42'),
    ('D43', 'D43'),
    ('D44', 'D44'),
    ('D45', 'D45'),
    ('D46', 'D46'),
    ('D47', 'D47'),
    ('D48', 'D48'),

]


# class Prontuario(models.Model):
#     id = models.IntegerField(primary_key=True)
#     paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
#     num_prontuario = models.CharField("NumProntuario", max_length=200)
#
#     def __str__(self):
#         return self.num_prontuario
#
#     class Meta:
#         verbose_name_plural = "Prontuarios"


class Anamnese(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, blank=True, null=True)
    prontuario = models.CharField("prontuario", max_length=200, blank=True)
    anamnese = models.TextField(verbose_name="Anamnese")

    def get_absolute_url(self):
        return reverse("anamnese_detalhes", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Anamneses"


class InfSaudeSistemica(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True)
    prontuario = models.CharField("prontuario", max_length=200, blank=True)
    antecedentes_familiares = models.TextField(verbose_name="Antecedentes Familiares", blank=True)
    medicamentos_em_uso = models.TextField(verbose_name="Medicamentos Em uso", blank=True)
    cirurgias_anteriores = models.TextField(verbose_name="Cirurgias Anteriores", blank=True)
    problemas_cardiacos = models.TextField(verbose_name="Problemas Cardiacos", blank=True)
    problemas_gastrointestinais = models.TextField(verbose_name="Problemas Gastrointestinais", blank=True)
    alteracoes_sanguineas = models.TextField(verbose_name="Alterações Sanguineas", blank=True)
    enfermidades_osseas = models.TextField(verbose_name="Enfermidades Ósseas", blank=True)
    problemas_pulmonares = models.TextField(verbose_name="Problemas Pulmonares", blank=True)
    alergias = models.TextField("alergias", blank=True)
    habitos = models.TextField(verbose_name="Hábitos", blank=True)
    observacao = models.TextField(verbose_name="Há Alguma Informação Sobre Sua Saúde Que Não Foi Perguntada?",
                                  blank=True)

    def get_absolute_url(self):
        return reverse("inf_sau_sis_detalhes", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Informações de Saúde Sistêmicas"


class ExameFisico(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True)
    prontuario = models.CharField("prontuario", max_length=200, blank=True)
    nodulos_linfaticos = models.TextField(verbose_name="Nódulos Linfáticos", blank=True)
    amigdalas = models.TextField(verbose_name="Amígdalas", blank=True)
    trigono_retromolar = models.TextField(verbose_name="Trígono Retromolar", blank=True)
    palato_duro = models.TextField(verbose_name="Palato Duro", blank=True)
    palato_mole = models.TextField(verbose_name="Palato Mole", blank=True)
    labios = models.TextField(verbose_name="Lábios", blank=True)
    pele = models.TextField(verbose_name="Pele", blank=True)
    atm = models.TextField(verbose_name="ATM", blank=True)
    vestibulo = models.TextField(verbose_name="Vestíbulo", blank=True)
    higiene_bucal = models.TextField(verbose_name="Higiene Bucal", blank=True)

    def get_absolute_url(self):
        return reverse("exa_fis_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return self.paciente.nome

    class Meta:
        verbose_name_plural = "Exames Fisicos"


class SinaisVitaisClinicos(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True)
    prontuario = models.CharField("prontuario", max_length=200, blank=True)
    pressao_arterial = models.TextField(verbose_name="Pressão Arterial", blank=True)
    pulso = models.TextField(verbose_name="Pulso", blank=True)
    respiracao = models.TextField(verbose_name="Respiração", blank=True)
    temperatura = models.TextField(verbose_name="Temperatura", blank=True)
    placa_visivel_16v = models.CharField(verbose_name="16V", choices=PLACA_VISIVEL, max_length=1)
    placa_visivel_11v = models.CharField(verbose_name="16V", choices=PLACA_VISIVEL, max_length=1)
    placa_visivel_26v = models.CharField(verbose_name="16V", choices=PLACA_VISIVEL, max_length=1)
    placa_visivel_36v = models.CharField(verbose_name="16V", choices=PLACA_VISIVEL, max_length=1)
    placa_visivel_31v = models.CharField(verbose_name="16V", choices=PLACA_VISIVEL, max_length=1)
    placa_visivel_46v = models.CharField(verbose_name="16V", choices=PLACA_VISIVEL, max_length=1)

    indice = models.CharField(verbose_name="Indíce", max_length=5, blank=True)
    resultado = models.CharField(verbose_name="Resultado", choices=CHOICES_RESULTADO, max_length=15, blank=True)

    def get_absolute_url(self):
        return reverse("sin_vit_cli_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return '{} - {}'.format(self.prontuario, self.paciente.nome)

    class Meta:
        verbose_name_plural = "Sinais Vitais Clinicos"


class PSR(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    prontuario = models.CharField("prontuario", max_length=200, blank=True)
    sextante_16v = models.CharField(verbose_name="Sextante 16V", choices=SEXTANTE, max_length=1)
    sextante_11v = models.CharField(verbose_name="Sextante 11V", choices=SEXTANTE, max_length=1)
    sextante_26v = models.CharField(verbose_name="Sextante 26V", choices=SEXTANTE, max_length=1)
    sextante_36v = models.CharField(verbose_name="Sextante 36V", choices=SEXTANTE, max_length=1)
    sextante_31v = models.CharField(verbose_name="Sextante 31V", choices=SEXTANTE, max_length=1)
    sextante_46v = models.CharField(verbose_name="Sextante 46V", choices=SEXTANTE, max_length=1)

    def get_absolute_url(self):
        return reverse("psr_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return '{}'.format(self.paciente.nome)

    class Meta:
        verbose_name_plural = "PSR's"


class SolicitacaoExamesComplementares(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    prontuario = models.CharField("prontuario", max_length=200, blank=True)
    sol_exa_com = models.TextField(verbose_name="Solicitação Exames Complementares", blank=True)

    def get_absolute_url(self):
        return reverse("sol_exa_com_detalhes", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Solicitações Exames Complementares"


# class ResultadoExamesComplementares(models.Model):
#     id = models.IntegerField(primary_key=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
#     res_exa_com = models.TextField(verbose_name="Resultado Exames Complementares")
#
#     def get_absolute_url(self):
#         return reverse("res_exa_com_detalhes", kwargs={"pk": self.pk})
#
#     class Meta:
#         verbose_name_plural = "Resultados de Exames Complementares"


class Estenografia(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nome = models.CharField(verbose_name="nome", choices=ESTENOGRAFIA_CHOICES, max_length=25, blank=True,
                            default="nenhuma")

    # def get_absolute_url(self):
    #     return reverse("anamnese_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Estenografia"


def estenografia_create():
    if len(Estenografia.objects.all()) == 0:
        e1 = Estenografia(nome='higido')
        e1.save()
        e2 = Estenografia(nome='mancha branca ativa')
        e2.save()
        e3 = Estenografia(nome='mancha inativa')
        e3.save()
        e4 = Estenografia(nome='lesao de carie primaria')
        e4.save()
        e5 = Estenografia(nome='lesao de carie cronica')
        e5.save()
        e6 = Estenografia(nome='restauracao defeituosa')
        e6.save()
        e7 = Estenografia(nome='restauracao em bom estado')
        e7.save()
        e8 = Estenografia(nome='necessidade de tratamento endodontico')
        e8.save()
        e9 = Estenografia(nome='tratamento endodontico concluido')
        e9.save()
        e10 = Estenografia(nome='extracao indicada')
        e10.save()
        e11 = Estenografia(nome='necessidade de protese')
        e11.save()
        e12 = Estenografia(nome='protese fixa concluida ou satisfatoria')
        e12.save()
        e13 = Estenografia(nome='dente ausente ou extraido')
        e13.save()
        e14 = Estenografia(nome='selante a fazer')
        e14.save()
        e15 = Estenografia(nome='selante satisfatorio')
        e15.save()
        e16 = Estenografia(nome='faceta de desgaste')
        e16.save()
        e17 = Estenografia(nome='fratura')
        e17.save()
        e18 = Estenografia(nome='doenca periodontal')
        e18.save()
        e19 = Estenografia(nome='anomalia de forma')
        e19.save()
        e20 = Estenografia(nome='defeito de esmalte ou dentina')
        e20.save()
        e21 = Estenografia(nome='supranumerario')
        e21.save()
        e22 = Estenografia(nome='restauracao ou protese concluida')
        e22.save()
        e23 = Estenografia(nome='tratamento endodontico concluido')
        e23.save()

    else:
        print("Estenografia OK!")





# class Tratamento(models.Model):
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField(auto_now=True)
#     nome = models.CharField(verbose_name="procedimento",
#                             choices=TRATAMENTO_CHOICES,
#                             max_length=100,
#                             blank=True, default='nenhum')
#
#     class Meta:
#         verbose_name_plural = "Tratamentos"
#
#     def __str__(self):
#         return self.nome


class Dente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    prontuario = models.CharField("prontuario", max_length=200, blank=True)
    nome = models.CharField(verbose_name="Dente", max_length=3, blank=True)
    distal = models.ManyToManyField(Estenografia, blank=True, related_name="dente_distal")
    oclusal = models.ManyToManyField(Estenografia, blank=True, related_name="dente_oclusal")
    mesial = models.ManyToManyField(Estenografia, blank=True, related_name="dente_mesial")
    lingual = models.ManyToManyField(Estenografia, blank=True, related_name="dente_lingual")
    vestibular = models.ManyToManyField(Estenografia, blank=True, related_name="dente_vestibular")

    def get_absolute_url(self):
        return reverse("sup18", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Dentes"

    def __str__(self):
        return '{} - {} - {}'.format(self.prontuario, self.paciente.nome, self.nome)


class Odontograma(models.Model):
    id = models.IntegerField(primary_key=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    prontuario = models.CharField("prontuario", max_length=200, blank=True)
    dente_18 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_18")
    dente_17 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_17")
    dente_16 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_16")
    dente_15 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_15")
    dente_14 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_14")
    dente_13 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_13")
    dente_12 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_12")
    dente_11 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_11")

    dente_21 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_21")
    dente_22 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_22")
    dente_23 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_23")
    dente_24 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_24")
    dente_25 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_25")
    dente_26 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_26")
    dente_27 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_27")
    dente_28 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_28")

    dente_48 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_48")
    dente_47 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_47")
    dente_46 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_46")
    dente_45 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_45")
    dente_44 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_44")
    dente_43 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_43")
    dente_42 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_42")
    dente_41 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_41")

    dente_31 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_31")
    dente_32 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_32")
    dente_33 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_33")
    dente_34 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_34")
    dente_35 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_35")
    dente_36 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_36")
    dente_37 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_37")
    dente_38 = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="odontograma_dente_38")

    def get_absolute_url(self):
        return reverse("odo_ini_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return '{}'.format(self.paciente.nome)

    class Meta:
        verbose_name_plural = "Odontogramas"


# class Atendimento(models.Model):
#     prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE,
#                                    blank=True,
#                                    related_name="atendimento_prontuario")
#     dente = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, related_name="atendimento_dente")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return '{} - {}'.format(self.prontuario.paciente.nome, self.prontuario)
#
#     class Meta:
#         verbose_name_plural = "Atendimentos"
