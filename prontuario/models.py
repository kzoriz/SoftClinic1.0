from django.db import models
from pacientes.models import Paciente
from django.urls import reverse

C_CHOICES = [
    ('SIM', 'SIM'),
    ('NAO', 'NÃO'),
]

DOENCA_CHOICES = [
    ('carie', 'Carie'),
    ('canal', 'Canal'),
    ('cáries', 'cáries'),
    ('gengivite', 'gengivite'),
    ('tártaro', 'tártaro'),
    ('infecções', 'infecções'),
    ('sensibilidade', 'sensibilidade'),
]

PROCEDIMENTO_CHOICES = [
    ('limpeza', 'limpeza'),
    ('remoção de tartaro', 'remoção de tartaro'),
    ('aplicacao de fluor', 'aplicacao de fluor'),
]


DENTE_CHOICES = [
    ('D12', 'D12'),
    ('D13', 'D13'),
    ('D14', 'D14'),
    ('D15', 'D15'),
    ('D16', 'D16'),
    ('D17', 'D17'),
    ('D18', 'D18'),
    ('D19', 'D19'),
    ('D20', 'D20'),
    ('D21', 'D21'),
    ('D22', 'D23'),
    ('D24', 'D24'),
    ('D25', 'D25'),
    ('D26', 'D26'),
    ('D27', 'D27'),
    ('D28', 'D28'),

]

class Prontuario(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    num_prontuario = models.CharField("NumProntuario", max_length=200)

    def __str__(self):
        return self.num_prontuario

    class Meta:
        verbose_name_plural = "Prontuarios"


class Doenca(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    doenca = models.TextField(verbose_name="Doença", choices=DOENCA_CHOICES)

    def get_absolute_url(self):
        return reverse("anamnese_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return self.doenca

    class Meta:
        verbose_name_plural = "Doenças"


class Tratamento(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    tratamento = models.TextField(verbose_name="Tratamento", choices=PROCEDIMENTO_CHOICES)

    def get_absolute_url(self):
        return reverse("anamnese_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return self.tratamento

    class Meta:
        verbose_name_plural = "Tratamentos"


class Anamnese(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    anamnese = models.TextField(verbose_name="Anamnese")

    def get_absolute_url(self):
        return reverse("anamnese_detalhes", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Anamneses"


class InfSaudeSistemica(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
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
        return self.prontuario.paciente.nome

    class Meta:
        verbose_name_plural = "Exames Fisicos"


class SinaisVitaisClinicos(models.Model):
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
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
        return '{}'.format(self.prontuario.paciente.nome)

    class Meta:
        verbose_name_plural = "Sinais Vitais Clinicos"


class PSR(models.Model):
    SEXTANTE = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    sextante_16v = models.CharField(verbose_name="Sextante 16V", choices=SEXTANTE, max_length=1)
    sextante_11v = models.CharField(verbose_name="Sextante 11V", choices=SEXTANTE, max_length=1)
    sextante_26v = models.CharField(verbose_name="Sextante 26V", choices=SEXTANTE, max_length=1)
    sextante_36v = models.CharField(verbose_name="Sextante 36V", choices=SEXTANTE, max_length=1)
    sextante_31v = models.CharField(verbose_name="Sextante 31V", choices=SEXTANTE, max_length=1)
    sextante_46v = models.CharField(verbose_name="Sextante 46V", choices=SEXTANTE, max_length=1)

    def get_absolute_url(self):
        return reverse("psr_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return '{}'.format(self.prontuario.paciente.nome)

    class Meta:
        verbose_name_plural = "PSR's"


class SolicitacaoExamesComplementares(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    sol_exa_com = models.TextField(verbose_name="Solicitação Exames Complementares", blank=True)

    def get_absolute_url(self):
        return reverse("sol_exa_com_detalhes", kwargs={"pk": self.pk})
    class Meta:
        verbose_name_plural = "Solicitações Exames Complementares"


class ResultadoExamesComplementares(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    res_exa_com = models.TextField(verbose_name="Resultado Exames Complementares")

    def get_absolute_url(self):
        return reverse("res_exa_com_detalhes", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Resultados de Exames Complementares"


class PlanoTratamentoI(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    plano_tratamento_i = models.TextField(verbose_name="Plano de Tratamento 1º Opção")

    def get_absolute_url(self):
        return reverse("pla_tra_ii_detalhes", kwargs={"pk": self.pk})
    class Meta:
        verbose_name_plural = "Planos de Tratamentos I"


class PlanoTratamentoII(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    plano_tratamento_ii = models.TextField(verbose_name="Plano de Tratamento 2º Opção")

    def get_absolute_url(self):
        return reverse("pla_tra_i_detalhes", kwargs={"pk": self.pk})
    class Meta:
        verbose_name_plural = "Planos de Tratamentos II"


# class EvolucaoPaciente(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
#     evolucao_paciente = models.TextField(verbose_name="Evolução do Paciente")
#
#     def get_absolute_url(self):
#         return reverse("evo_pac_detalhes", kwargs={"pk": self.pk})


# class Dente(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     #prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE, blank=True)
#     doencas = models.ForeignKey(Doenca, on_delete=models.CASCADE, blank=True)
#     # dente = models.CharField(verbose_name="Dente", choices=DENTE_CHOICES, max_length=3, blank=True)
#
#     # def get_absolute_url(self):
#     #     return reverse("anamnese_detalhes", kwargs={"pk": self.pk})
#
#     class Meta:
#         verbose_name_plural = "Dentes"
#
#     def __str__(self):
#         return self.dente


class OdontogramaInicial(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE, blank=True)

    d11 = models.ManyToManyField(Doenca, blank=True, related_name="Dente11")
    d12 = models.ManyToManyField(Doenca, blank=True, related_name="Dente12")
    d13 = models.ManyToManyField(Doenca, blank=True, related_name="Dente13")
    d14 = models.ManyToManyField(Doenca, blank=True, related_name="Dente14")
    d15 = models.ManyToManyField(Doenca, blank=True, related_name="dente15")
    d16 = models.ManyToManyField(Doenca, blank=True, related_name="Dente16")
    d17 = models.ManyToManyField(Doenca, blank=True, related_name="Dente17")
    d18 = models.ManyToManyField(Doenca, blank=True, related_name="Dente18")

    d21 = models.ManyToManyField(Doenca, blank=True, related_name="Dente21")
    d22 = models.ManyToManyField(Doenca, blank=True, related_name="Dente22")
    d23 = models.ManyToManyField(Doenca, blank=True, related_name="Dente23")
    d24 = models.ManyToManyField(Doenca, blank=True, related_name="Dente24")
    d25 = models.ManyToManyField(Doenca, blank=True, related_name="dente25")
    d26 = models.ManyToManyField(Doenca, blank=True, related_name="Dente26")
    d27 = models.ManyToManyField(Doenca, blank=True, related_name="Dente27")
    d28 = models.ManyToManyField(Doenca, blank=True, related_name="Dente28")

    d31 = models.ManyToManyField(Doenca, blank=True, related_name="Dente31")
    d32 = models.ManyToManyField(Doenca, blank=True, related_name="Dente32")
    d33 = models.ManyToManyField(Doenca, blank=True, related_name="Dente33")
    d34 = models.ManyToManyField(Doenca, blank=True, related_name="Dente34")
    d35 = models.ManyToManyField(Doenca, blank=True, related_name="dente35")
    d36 = models.ManyToManyField(Doenca, blank=True, related_name="Dente36")
    d37 = models.ManyToManyField(Doenca, blank=True, related_name="Dente37")
    d38 = models.ManyToManyField(Doenca, blank=True, related_name="Dente38")

    d41 = models.ManyToManyField(Doenca, blank=True, related_name="Dente41")
    d42 = models.ManyToManyField(Doenca, blank=True, related_name="Dente42")
    d43 = models.ManyToManyField(Doenca, blank=True, related_name="Dente43")
    d44 = models.ManyToManyField(Doenca, blank=True, related_name="Dente44")
    d45 = models.ManyToManyField(Doenca, blank=True, related_name="Dente45")
    d46 = models.ManyToManyField(Doenca, blank=True, related_name="Dente46")
    d47 = models.ManyToManyField(Doenca, blank=True, related_name="Dente47")
    d48 = models.ManyToManyField(Doenca, blank=True, related_name="Dente48")

    def get_absolute_url(self):
        return reverse("odo_ini_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return '{}'.format(self.prontuario.paciente.nome)

    class Meta:
        verbose_name_plural = "Odontogramas Iniciais"


class Procedimento(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    dente_tratado= models.CharField(verbose_name="Dente", choices=DENTE_CHOICES, max_length=3, blank=True)
    # procedimento_realizado = models.CharField(verbose_name="Procedimento Realizado",
    #                                           choices=PROCEDIMENTO_CHOICES, blank=True, max_length=100)

    d11 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente11")
    d12 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente12")
    d13 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente13")
    d14 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente14")
    d15 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente15")
    d16 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente16")
    d17 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente17")
    d18 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente18")

    d21 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente21")
    d22 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente22")
    d23 = models.ManyToManyField(Tratamento, blank=True, related_name="tratamentoDente23")
    d24 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente24")
    d25 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente25")
    d26 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente26")
    d27 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente27")
    d28 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente28")

    d31 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente31")
    d32 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente32")
    d33 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente33")
    d34 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente34")
    d35 = models.ManyToManyField(Tratamento, blank=True, related_name="Tratamentodente35")
    d36 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente36")
    d37 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente37")
    d38 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente38")

    d41 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente41")
    d42 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente42")
    d43 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente43")
    d44 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente44")
    d45 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente45")
    d46 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente46")
    d47 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente47")
    d48 = models.ManyToManyField(Tratamento, blank=True, related_name="TratamentoDente48")

    # def get_absolute_url(self):
    #     return reverse("anamnese_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return '{} - {}'.format(self.prontuario.paciente.nome, self.prontuario)

    class Meta:
        verbose_name_plural = "Procedimentos"