from django.db import models
from pacientes.models import Paciente
from django.urls import reverse

C_CHOICES = [
    ('SIM', 'SIM'),
    ('NAO', 'NÃO'),
]


class Prontuario(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    num_prontuario = models.CharField("NumProntuario", max_length=200)

    def __str__(self):
        return self.num_prontuario


'''
class DadosMedicos(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    temp_trat = models.CharField("Tempo de Tratamento", max_length=50, blank=True)
    causa = models.CharField("Causa", max_length=50, blank=True)
    crm_med = models.CharField("CRM Medico", max_length=50, blank=True)
    tel_med = models.CharField("Telefone Medico", max_length=25, blank=True)
    cont_urg = models.CharField("Contato de Urgencia", max_length=25, blank=True)

    def __str__(self):
        return self.prontuario.paciente.nome


class Medicamentos(models.Model):

    PRONTUARIO_CHOICES = [
        ('Med1', 'Medicamnto1'),
        ('Med2', 'Medicamnto2'),
        ('Med3', 'Medicamnto3'),
        ('Med4', 'Medicamnto4'),
        ('Med5', 'Medicamnto5'),
    ]

    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    medicamento = models.CharField("Medicamento", max_length=100, choices=PRONTUARIO_CHOICES, blank=True)
    cirur_real = models.CharField("Cirurgia Realizada", max_length=50, blank=True)
    dst = models.CharField("DST", max_length=50, blank=True)
    anticoncepcional = models.CharField("Anticoncepcional", max_length=50, blank=True)
    cardiopatia = models.CharField("Cardiopatias", max_length=50, blank=True)
    prob_gastri = models.CharField("Problemas Gastricos", max_length=50, blank=True)
    prob_pulmo = models.CharField("Problemas Pulmonares", max_length=50, blank=True)
    alt_sang = models.CharField("Alterações Sanguineas", max_length=50, blank=True)
    enf_ossea_infla = models.CharField("Infermidades Osséa Inflamatorias", max_length=50, blank=True)
    habitos = models.CharField("Hábitos", max_length=50, blank=True)
    alergias = models.CharField("Alergias", max_length=50, blank=True)

    def __str__(self):
        return self.prontuario.paciente.nome


class Saude(models.Model):

    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    diabetes = models.CharField("Diabetes", max_length=3, choices=C_CHOICES)
    gravida = models.CharField("Grávida", max_length=3, choices=C_CHOICES)
    plan_grav = models.CharField("Planeja Gravidez", max_length=3, choices=C_CHOICES)
    hipertensao = models.CharField("Hipertensão", max_length=3, choices=C_CHOICES)
    sangramento = models.CharField("Sangramento", max_length=3, choices=C_CHOICES)
    epilepsia = models.CharField("Epilepsia", max_length=3, choices=C_CHOICES)
    prob_ren = models.CharField("Problemas Renais", max_length=3, choices=C_CHOICES)
    doenc_mental = models.CharField("Doença Mental", max_length=3, choices=C_CHOICES)
    rad_terapia = models.CharField("Rádio Terapia", max_length=3, choices=C_CHOICES)
    qui_terapia = models.CharField("Quimioterapia", max_length=3, choices=C_CHOICES)
    hepatite = models.CharField("Hepatite", max_length=3, choices=C_CHOICES)
    articulacao = models.CharField("Articulações", max_length=3, choices=C_CHOICES)
    protese = models.CharField("Prótese", max_length=3, choices=C_CHOICES)
    hiv = models.CharField("HIV", max_length=3, choices=C_CHOICES)
    fumante = models.CharField("Fumante", max_length=3, choices=C_CHOICES)
    herpes = models.CharField("Herpes", max_length=3, choices=C_CHOICES)
    bebida = models.CharField("Bebida", max_length=3, choices=C_CHOICES)
    inf_add = models.TextField("Informações Adicionais")


class ExameFisicoIB(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    atm = models.CharField("ATM", max_length=50, blank=True)
    lab_sup = models.CharField("Labio Superior", max_length=50, blank=True)
    lab_inf = models.CharField("LabioInferior", max_length=50, blank=True)
    com_labial = models.CharField("Comissura Labial", max_length=50, blank=True)
    muc_jugal = models.CharField("Mucosa Jugal", max_length=50, blank=True)
    palato_duro = models.CharField("Palato Duro", max_length=50, blank=True)
    palato_mole = models.CharField("Palato Mole", max_length=50, blank=True)
    tonsilas = models.CharField("Tonsilas", max_length=50, blank=True)
    hig_oral = models.CharField("Higiene Oral", max_length=50, blank=True)
    sang_gengival = models.CharField("Sangramento Gengival", max_length=50, blank=True)
    calculo = models.CharField("Cálculo", max_length=50, blank=True)


class PlanoTratamento(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    reg_dente = models.CharField("Região do Dente", max_length=50, blank=True)
    procedimento = models.CharField("Procedimento", max_length=50, blank=True)


class CondOclusal(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    tipo_co = models.CharField("Tipo CO", max_length=100, blank=True)


class Odontograma(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    dente = models.CharField("Dente", max_length=100, blank=True)
    condicao = models.CharField("Condição", max_length=100, blank=True)


class PSR(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    sextante = models.CharField("Sextante", max_length=100, blank=True)
    classificacao = models.CharField("Classificação", max_length=100, blank=True)



class Procedimento(models.Model):
    prontuario = models.CharField("NumProntuario", max_length=200)
    cpf = models.CharField("CPF", max_length=100, blank=True)
    reg_dente = models.CharField("Região do Dente", max_length=50, blank=True)
    procedimento = models.CharField("Procedimento", max_length=50, blank=True)

    def __str__(self):
        return self.cpf
'''


class Anamnese(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    anamnese = models.TextField(verbose_name="Anamnese")

    def get_absolute_url(self):
        return reverse("anamnese_detalhes", kwargs={"pk": self.pk})


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

    indice = models.CharField(verbose_name="Indíce", max_length=5,blank=True)
    resultado = models.CharField(verbose_name="Resultado", choices=CHOICES_RESULTADO, max_length=15, blank=True)

    def get_absolute_url(self):
        return reverse("sin_vit_cli_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return '{}'.format(self.prontuario.paciente.nome)


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



class OdontogramaInicial(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    d11 = models.TextField(verbose_name="11")
    d12 = models.TextField(verbose_name="12")
    d13 = models.TextField(verbose_name="13")
    d14 = models.TextField(verbose_name="14")
    d15 = models.TextField(verbose_name="15")
    d16 = models.TextField(verbose_name="16")
    d17 = models.TextField(verbose_name="17")
    d18 = models.TextField(verbose_name="18")
    d21 = models.TextField(verbose_name="21")
    d22 = models.TextField(verbose_name="22")
    d23 = models.TextField(verbose_name="23")
    d24 = models.TextField(verbose_name="24")
    d25 = models.TextField(verbose_name="25")
    d26 = models.TextField(verbose_name="26")
    d27 = models.TextField(verbose_name="27")
    d28 = models.TextField(verbose_name="28")
    d31 = models.TextField(verbose_name="31")
    d32 = models.TextField(verbose_name="32")
    d33 = models.TextField(verbose_name="33")
    d34 = models.TextField(verbose_name="34")
    d35 = models.TextField(verbose_name="35")
    d36 = models.TextField(verbose_name="36")
    d37 = models.TextField(verbose_name="37")
    d38 = models.TextField(verbose_name="38")
    d41 = models.TextField(verbose_name="41")
    d42 = models.TextField(verbose_name="42")
    d43 = models.TextField(verbose_name="43")
    d44 = models.TextField(verbose_name="44")
    d45 = models.TextField(verbose_name="45")
    d46 = models.TextField(verbose_name="46")
    d47 = models.TextField(verbose_name="47")
    d48 = models.TextField(verbose_name="48")

    def get_absolute_url(self):
        return reverse("odo_ini_detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return '{}'.format(self.prontuario.paciente.nome)


class SolicitacaoExamesComplementares(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    sol_exa_com = models.TextField(verbose_name="Solicitação exames Complementares")

    def get_absolute_url(self):
        return reverse("sol_exa_com_detalhes", kwargs={"pk": self.pk})


class ResultadoExamesComplementares(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    res_exa_com = models.TextField(verbose_name="Resulatdo Exames Complementares")

    def get_absolute_url(self):
        return reverse("res_exa_com_detalhes", kwargs={"pk": self.pk})


class PlanoTratamentoI(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    plano_tratamento_i = models.TextField(verbose_name="Plano de Tratamento 1º Opção")

    def get_absolute_url(self):
        return reverse("pla_tra_ii_detalhes", kwargs={"pk": self.pk})


class PlanoTratamentoII(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    plano_tratamento_ii = models.TextField(verbose_name="Plano de Tratamento 2º Opção")

    def get_absolute_url(self):
        return reverse("pla_tra_i_detalhes", kwargs={"pk": self.pk})


class EvolucaoPaciente(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    evolucao_paciente = models.TextField(verbose_name="Evolução do Paciente")

    def get_absolute_url(self):
        return reverse("evo_pac_detalhes", kwargs={"pk": self.pk})
