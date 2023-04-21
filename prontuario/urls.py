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
    path("odo-detalhes/<int:pk>", odon_detalhes, name="odon_detalhes"),
    path("odo-edit/<int:pk>/", OdontogramaUpdate.as_view(), name="odo_edit"),
    path("sol-exa-com-detalhes/<int:pk>/", sol_exa_com_detalhes, name="sol_exa_com_detalhes"),
    path("sol-exa-com-edit/<int:pk>/", SolicitacaoExamesComplementaresUpdate.as_view(), name="sol_exa_com_edit"),

    path("sup-18/<int:pk>", sup18, name="sup18"),
    path("sup-18-edit/<int:pk>", sup18_edit, name="sup18_edit"),
    path("sup-17/<int:pk>/", sup17, name="sup17"),
]
