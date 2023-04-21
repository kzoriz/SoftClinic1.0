
from django.db import models
from django.urls import reverse

SEXO_BIOLOGICO = [
    ("MASCULINO", "masculino"),
    ("FEMININO", "feminino"),
]

RACA = [
    ("BRANCO", "branco"),
    ("PARDO", "pardo"),
    ("PRETO", "preto"),
    ("INDIGENA", "indigena"),
    ("AMARELO", "amarelo"),
]

ESTADO_CIVIL = [
    ("SOLTEIRO", "Solteiro"),
    ("CASADO", "Casado"),
    ("SEPARADO", "Separado"),
    ("DIVORCIADO", "Divorciado"),
    ("VIUVO", "Viúvo"),
]
A_F = [
    ("S", "Sim"),
    ("N", "Não"),
]

GRAU_INSTRUCAO = [
    ('NIVEL 1', (
        ('ANALFABETO', 'Analfabeto'),
        ('5º_ANO_INCOMPLETO', 'Até 5º Ano Incompleto'),
        ('5º_ANO_COMPLETO', 'Até 5º Ano completo'),
        ('6º_AO_9º_Ano_do_Fundamental', '6º ao 9º Ano do Fundamental'),
    )
     ),
    ('NIVEL 2', (
        ('Fundamental_Completo', 'Fundamental Completo'),
        ('Médio Incompleto', 'Médio Incompleto'),
    )
     ),
    ('NIVEL 3', (
        ('Médio Completo', 'Médio Completo'),
        ('Superior Incompleto', 'Superior Incompleto'),
    )
     ),
    ('NIVEL 4', (
        ('Superior Completo', 'Superior Completo'),
    )
     ),
    ('NIVEL 5', (
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado'),
    )
     ),
]

UF_CHOICES = (
    ('AC', 'Acre'),
    ('AM', 'Amazonas'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
)


class Paciente(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.IntegerField(primary_key=True)
    prontuario = models.CharField("prontuario", max_length=200, blank=True)
    nome = models.CharField(verbose_name="Nome", max_length=200)
    nome_social = models.CharField(verbose_name="Nome Social", max_length=200, blank=True)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento", auto_now=False, auto_now_add=False,
                                       blank=True)
    sexo_biologico = models.CharField(verbose_name="Sexo Biologico", max_length=200, blank=True)
    rg = models.CharField(verbose_name="RG", max_length=200, blank=True)
    cpf = models.CharField(verbose_name="CPF", max_length=200, blank=True)
    raca = models.CharField(verbose_name="Raça", max_length=200, blank=True)
    estado_civil = models.CharField(verbose_name="Estado Civil", max_length=200, blank=True)
    grau_instrucao = models.CharField(verbose_name="Grau de Instrução", max_length=200, blank=True)
    endereco = models.CharField(verbose_name="Endereço", max_length=200, blank=True)
    cep = models.CharField(verbose_name="CEP", max_length=200, blank=True)
    bairro = models.CharField(verbose_name="Bairro", max_length=200, blank=True)
    cidade = models.CharField(verbose_name="Cidade", max_length=200, blank=True)
    uf = models.CharField(verbose_name="UF", max_length=2, blank=True)
    telefone_celular = models.CharField(verbose_name="Telefone Celular", max_length=200, blank=True)
    informacoes_complementares = models.TextField(verbose_name="Informações Complementares", blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("paciente_detalhes", kwargs={"pk": self.pk})


class PacienteInfantil(models.Model):
    responsavel = models.CharField(verbose_name="Reponsavel", max_length=200)
    nome = models.CharField(verbose_name="Nome", max_length=200)
    nome_social = models.CharField(verbose_name="Nome Social", max_length=200, blank=True)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento", auto_now=False, auto_now_add=False)
    sexo_biologico = models.CharField(verbose_name="Sexo Biologico", max_length=200)
    rg = models.CharField(verbose_name="RG", max_length=200, blank=True)
    cpf = models.CharField(verbose_name="CPF", max_length=200)
    raca = models.CharField(verbose_name="Raça", max_length=200)
    estado_civil = models.CharField(verbose_name="Estado Civil", max_length=200)
    grau_instrucao = models.CharField(verbose_name="Grau de Instrução", max_length=200)
    endereco = models.CharField(verbose_name="Endereço", max_length=200)
    cep = models.CharField(verbose_name="CEP", max_length=200)
    bairro = models.CharField(verbose_name="Bairro", max_length=200)
    cidade = models.CharField(verbose_name="Cidade", max_length=200)
    uf = models.CharField(verbose_name="UF", max_length=200)
    telefone_celular = models.CharField(verbose_name="Telefone Celular", max_length=200)
    informacoes_complementares = models.TextField(verbose_name="Informações Complementares")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Paciente Infantil"
        verbose_name_plural = "Pacientes Infantis"


class Teste(models.Model):
    testando = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.testando}"

    class Meta:
        verbose_name_plural = "Testes"


class Teste2(models.Model):
    testando = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.testando}"

    class Meta:
        verbose_name_plural = "Teste2s"
