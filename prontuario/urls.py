from django.urls import path
from prontuario.views import *

urlpatterns = [
    path("anamnese-detalhes/<int:pk>/", anamnese_detalhes, name="anamnese_detalhes"),
    path("anamnese-edit/<int:pk>/", AnamneseUpdate.as_view(), name="anamnese_edit"),
    path("inf-sau-sis-detalhes/<int:pk>/", inf_saude_sistemica_detalhes, name="inf_sau_sis_detalhes"),
    path("inf-sau-sis-edit/<int:pk>/", InfSaudeSistemicaUpdate.as_view(), name="inf_sau_sis_edit"),
    path("exa-fis-detalhes/<int:pk>/", exame_fisico_detalhes, name="exa_fis_detalhes"),
    path("exa-fis-edit/<int:pk>/", ExameFisicoUpdate.as_view(), name="exa_fis_edit"),
    path("sin-vit-cli-detalhes/<int:pk>/", sinais_vitais_clinicos_detalhes, name="sin_vit_cli_detalhes"),
    path("sin-vit-cli-edit/<int:pk>/", SinaisVitaisClinicosUpdate.as_view(), name="sin_vit_cli_edit"),
    path("psr-detalhes/<int:pk>/", psr_detalhes, name="psr_detalhes"),
    path("psr-edit/<int:pk>/", PSRUpdate.as_view(), name="psr_edit"),
    path("odo-detalhes/<str:prontuario>", odon_detalhes, name="odon_detalhes"),
    path("odo-edit/<int:pk>/", OdontogramaUpdate.as_view(), name="odo_edit"),
    path("sol-exa-com-detalhes/<int:pk>/", sol_exa_com_detalhes, name="sol_exa_com_detalhes"),
    path("sol-exa-com-edit/<int:pk>/", SolicitacaoExamesComplementaresUpdate.as_view(), name="sol_exa_com_edit"),
    path("res-exa-com-detalhes/<int:pk>/", res_exa_com_detalhes, name="res_exa_com_detalhes"),
    path("res-exa-com-edit/<int:pk>/", ResultadoExamesComplementaresUpdate.as_view(), name="res_exa_com_edit"),
    path("odontogramas/", odontogramas, name="odontograma"),
    # path("pla-tra-i-detalhes/<int:pk>/", pla_tra_i_detalhes, name="pla_tra_i_detalhes"),
    # path("pla-tra-i-edit/<int:pk>/", PlanoTratamentoIUpdate.as_view(), name="pla_tra_i_edit"),
    # path("pla-tra-ii-detalhes/<int:pk>/", pla_tra_ii_detalhes, name="pla_tra_ii_detalhes"),
    # path("pla-tra-ii-edit/<int:pk>/", PlanoTratamentoIIUpdate.as_view(), name="pla_tra_ii_edit"),
    # path("evo-pac-detalhes/<int:pk>/", evo_pac_detalhes, name="evo_pac_detalhes"),
    # path("evo-pac-edit/<int:pk>/", EvolucaoPacienteUpdate.as_view(), name="evo_pac_edit"),
    path("sup-18", sup18, name="sup18"),
    path("sup-17", sup17, name="sup17"),

]