from django.urls import path
from django.contrib.auth import views as auth_views

from distribuicao.views import distribuir_paciente_index, DisciplinaCreateView,\
    disciplinas, disciplina_detalhes, DisciplinaUpdate, DisciplinaDelete

urlpatterns = [
    path("distribuir-pacientes/", distribuir_paciente_index, name="distribuir_pacientes_menu"),
    path("cadastro-disciplina/", DisciplinaCreateView.as_view() , name="cadastro_disciplina"),
    path("disciplinas/", disciplinas, name="disciplinas"),
    path("disciplina/detalhes/<int:pk>/", disciplina_detalhes, name="disciplina_detalhes"),
    path("disciplinas/editar/<int:pk>/", DisciplinaUpdate.as_view(), name="disciplina_editar"),
    path("disciplina/delete/<int:pk>/", DisciplinaDelete.as_view(), name="disciplina_delete"),


]