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
    ('nenhuma', 'nenhuma'),
]

PROCEDIMENTO_CHOICES = [
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


class Prontuario(models.Model):
    id = models.IntegerField(primary_key=True)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    num_prontuario = models.CharField("NumProntuario", max_length=200)

    def __str__(self):
        return self.num_prontuario

    class Meta:
        verbose_name_plural = "Prontuarios"


class Anamnese(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    anamnese = models.TextField(verbose_name="Anamnese")

    def get_absolute_url(self):
        return reverse("anamnese_detalhes", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Anamneses"


class InfSaudeSistemica(models.Model):
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
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

    id = models.IntegerField(primary_key=True)
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

    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    sol_exa_com = models.TextField(verbose_name="Solicitação Exames Complementares", blank=True)

    def get_absolute_url(self):
        return reverse("sol_exa_com_detalhes", kwargs={"pk": self.pk})
    class Meta:
        verbose_name_plural = "Solicitações Exames Complementares"


class ResultadoExamesComplementares(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    res_exa_com = models.TextField(verbose_name="Resultado Exames Complementares")

    def get_absolute_url(self):
        return reverse("res_exa_com_detalhes", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Resultados de Exames Complementares"


class Doenca(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nome = models.TextField(verbose_name="Doença", choices=DOENCA_CHOICES, blank=True, default="nenhuma")

    def get_absolute_url(self):
        return reverse("anamnese_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Doenças"


class Procedimento(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    nome = models.CharField(verbose_name="procedimento",
                            choices=PROCEDIMENTO_CHOICES,
                            max_length=100,
                            blank=True, default='nenhum')


class Dente(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE, related_name="dente", blank=True)
    nome = models.CharField(verbose_name="Dente", choices=DENTE_CHOICES, max_length=3, blank=True)
    procedimento = models.ManyToManyField(Procedimento, blank=True, related_name="dente")
    doenca = models.ManyToManyField(Doenca, blank=True, related_name="dente")

    # def get_absolute_url(self):
    #     return reverse("anamnese_detalhes", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Dentes"

    def __str__(self):
        return self.nome


class Diagnostico(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    #doenca = models.ManyToManyField(Doenca, blank=True, related_name="diagnostico")
    dente = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, default="D11")

    def get_absolute_url(self):
        return reverse("anamnese_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return '{}'.format(self.dente.nome)

    class Meta:
        verbose_name_plural = "Diagnosticos"


class OdontogramaInicial(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, blank=True, null=True, related_name="odontograma_inicial")

    def get_absolute_url(self):
        return reverse("odo_ini_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return '{} - {}'.format(self.prontuario.paciente.nome, self.diagnostico)

    class Meta:
        verbose_name_plural = "Odontogramas Iniciais"


class Odontograma(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE, related_name="prontuario")
    odontograma_inicial = models.OneToOneField(OdontogramaInicial,
                                               on_delete=models.CASCADE,
                                               related_name="odontograma_inicial",
                                               blank=True, null=True)

    def get_absolute_url(self):
        return reverse("odo_ini_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return '{}'.format(self.prontuario.paciente.nome)

    class Meta:
        verbose_name_plural = "Odontogramas"


class Atendimento(models.Model):
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE, blank=True, related_name="atendimento")
    #procedimento = models.ManyToManyField(Procedimento, blank=True, related_name="atendimento")
    dente = models.ForeignKey(Dente, on_delete=models.CASCADE, blank=True, related_name="atendimento")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.prontuario.paciente.nome, self.prontuario)

    class Meta:
        verbose_name_plural = "Atendimentos"
