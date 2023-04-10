from django.contrib import admin

# Register your models here.
from prontuario.models import *


admin.site.register(Prontuario)
admin.site.register(Anamnese)
admin.site.register(InfSaudeSistemica)
admin.site.register(ExameFisico)
admin.site.register(SinaisVitaisClinicos)
admin.site.register(PSR)
# admin.site.register(OdontogramaInicial)
admin.site.register(SolicitacaoExamesComplementares)
admin.site.register(ResultadoExamesComplementares)
# admin.site.register(PlanoTratamentoI)
# admin.site.register(PlanoTratamentoII)
#admin.site.register(EvolucaoPaciente)
admin.site.register(Atendimento)
admin.site.register(Dente)
admin.site.register(Estenografia)
# admin.site.register(Diagnostico)
admin.site.register(Odontograma)
admin.site.register(Tratamento)

