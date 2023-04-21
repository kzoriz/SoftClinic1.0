# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.urls import reverse_lazy
#
#
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import ListView
# # from .models import Disciplina
# # Create your views here.
# def distribuir_paciente_index(request):
#     return render(request, "distribuicao/distribuir_paciente_index.html" )
#
#
# class DisciplinaCreateView(CreateView):
#     model = Disciplina
#     fields = "__all__"
#     template_name = "distribuicao/cadastro_disciplina.html"
#     success_url = reverse_lazy("opcoes")
#
#
#
# def disciplinas(request):
#     todas_disciplinas = Disciplina.objects.all()
#
#     context = {
#         "nome_pagina": "DISCIPLINAS",
#         "todas_disciplinas": todas_disciplinas,
#
#     }
#     return render(request, "distribuicao/disciplinas.html", context)
#
# def disciplina_detalhes(request, pk = None):
#     disciplina = Disciplina.objects.get(pk=pk)
#     context = {
#         'disciplina': disciplina
#     }
#     return render(request, 'distribuicao/disciplina_detalhes.html', context)
#
# class DisciplinaUpdate(LoginRequiredMixin, UpdateView):
#     login_url = reverse_lazy("login")
#     model = Disciplina
#     fields = "__all__"
#     template_name = "distribuicao/disciplina_editar.html"
#     success_url = reverse_lazy("disciplinas")
#
# class DisciplinaDelete(LoginRequiredMixin,DeleteView):
#     login_url = reverse_lazy("login")
#     model = Disciplina
#     template_name = "distribuicao/disciplina_delete.html"
#     success_url = reverse_lazy("disciplinas")