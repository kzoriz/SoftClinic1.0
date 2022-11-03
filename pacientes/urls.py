from django.urls import path, include
from pacientes.views import *

urlpatterns = [

    path("pacientes/", pacientes, name="pacientes"),
    path("pacientes/registrar/", registrar_paciente, name="paciente_registrar"),
    path("pacientes/registrar-inf/", registrar_paciente_inf, name="paciente_registrar_inf"),
    path("pacientes/detalhes/<int:pk>/", paciente_detalhes, name="paciente_detalhes"),
    path("pacientes/detalhes-inf/<int:pk>/", paciente_detalhes_inf, name="paciente_detalhes_inf"),
    path("pacientes/editar/<int:pk>/", PacienteUpdate.as_view(), name="paciente_editar"),
    path("pacientes/editar-inf/<int:pk>/", PacienteInfantilUpdate.as_view(), name="paciente_editar_inf"),
    path("paciente/delete/<int:pk>/", PacienteDelete.as_view(), name="paciente_delete"),
    path("paciente/delete-inf/<int:pk>/", PacienteInfantilDelete.as_view(), name="paciente_delete_inf"),
    path("agenda/", agenda, name="agenda"),
    path("", inicio, name="inicio"),
    path("opcoes/", opcoes, name="opcoes"),

    path("pacientes-menu/", registrar_paciente_2, name="pacientes_menu"),
]
####
