from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from prontuario.models import *
from django.views.decorators.clickjacking import xframe_options_sameorigin


def anamnese_detalhes(request, pk=None):
    object = Anamnese.objects.get(pk=pk)
    paciente = Paciente.objects.get(pk=pk)
    context = {
        'object': object,
        'paciente': paciente,
    }
    return render(request, 'prontuario/anamnese_detalhes.html', context)


class AnamneseUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Anamnese'}
    model = Anamnese
    fields = ['anamnese', ]
    template_name = "prontuario/anamnese_editar.html"
    success_message = "Anamnese atualizada com Sucesso!"


def inf_saude_sistemica_detalhes(request, pk=None):
    object = InfSaudeSistemica.objects.get(pk=pk)
    paciente = Paciente.objects.get(pk=pk)
    context = {
        'object': object,
        'paciente': paciente,
    }
    return render(request, 'prontuario/inf_saude_sistemica.html', context)


class InfSaudeSistemicaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Informações de Saúde Sistemica'}
    model = InfSaudeSistemica
    fields = ['antecedentes_familiares', 'medicamentos_em_uso', 'cirurgias_anteriores', 'problemas_cardiacos',
              'problemas_gastrointestinais', 'alteracoes_sanguineas', 'enfermidades_osseas', 'problemas_pulmonares',
              'alergias', 'habitos', 'observacao']
    template_name = "prontuario/inf_saude_sistemica_editar.html"
    success_message = "Informações de saúde Sistêmica atualizadas com Sucesso!"


def exame_fisico_detalhes(request, pk=None):
    object = ExameFisico.objects.get(pk=pk)
    paciente = Paciente.objects.get(pk=pk)
    context = {
        'object': object,
        'paciente': paciente,
    }
    return render(request, 'prontuario/exame_fisico_detalhes.html', context)


class ExameFisicoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Exame Fisico'}
    model = ExameFisico
    fields = ['nodulos_linfaticos', 'amigdalas', 'trigono_retromolar', 'palato_duro', 'palato_mole',
              'labios', 'pele', 'atm', 'vestibulo', 'higiene_bucal']
    template_name = "prontuario/exame_fisico_editar.html"
    success_message = "Exame Físico atualizado com Sucesso!"


def sinais_vitais_clinicos_detalhes(request, pk=None):
    object = SinaisVitaisClinicos.objects.get(pk=pk)
    paciente = Paciente.objects.get(pk=pk)
    context = {
        'object': object,
        'paciente': paciente,
    }
    return render(request, 'prontuario/sinais_vitais_clinicos_detalhes.html', context)


class SinaisVitaisClinicosUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Sinais Vitais Clinicos'}
    model = SinaisVitaisClinicos
    fields = ['pressao_arterial', 'pulso', 'respiracao', 'temperatura', 'placa_visivel_16v',
              'placa_visivel_11v', 'placa_visivel_26v', 'placa_visivel_36v', 'placa_visivel_31v', 'placa_visivel_46v']
    template_name = "prontuario/sinais_vitais_clinicos_editar.html"
    # template_name = "prontuario/padrao.html"
    success_message = "Exame Sinais Vitais Clinicos atualizado com Sucesso!"


def psr_detalhes(request, pk=None):
    object = PSR.objects.get(pk=pk)
    paciente = Paciente.objects.get(pk=pk)
    context = {
        'object': object,
        'paciente': paciente,
    }
    return render(request, 'prontuario/psr_detalhes.html', context)


class PSRUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'PSR'}
    model = PSR
    fields = ['sextante_16v', 'sextante_11v', 'sextante_26v', 'sextante_36v', 'sextante_31v',
              'sextante_46v']
    template_name = "prontuario/psr_editar.html"
    success_message = "Exame PSR atualizado com Sucesso!"


def odon_detalhes(request, pk=None):
    object = Odontograma.objects.get(pk=pk)
    paciente = Paciente.objects.get(pk=pk)
    dente = list(object.dente_17.distal.all())
    dente2 = []
    print('##########################################################################################################################')
    print(type(dente))
    for i in dente:
        print(i)
        i = str(i)
        dente2.append(i)
        print(type(i))
    for i in dente2:
        print(i, type(i))
    context = {
        'object': object,
        'paciente': paciente,
        'dente': dente2,

    }
    return render(request, 'prontuario/odon_detalhes.html', context)


# def odon_update(request, pk=None):
#
#
#     if request.method == 'POST':
#         odontograma = Odontograma.objects.get(pk=pk)
#         d_18 = Dente.objects.filter(Dente.prontuario == odontograma.prontuario and Dente.nome == '18')
#         distal = request.POST['distal_18']
#
#         d = d_18(distal=distal)
#         d.save()
#
#         messages.success(request, "#")
#         return redirect("pacientes")
#     return render(request, "prontuario/Dentes/dentadura-sup-18.html")


# class OdonUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     login_url = reverse_lazy("login")
#     extra_context = {'nome_pagina': 'Odontograma Inicial'}
#     model = Dente
#     fields = ['distal']
#     template_name = "prontuario/Dentes/dentadura-sup-18.html"
#     success_message = "Odontograma Inicial Atualizado com Sucesso!"


class OdontogramaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Odontograma Inicial'}
    model = Odontograma
    fields = ['d11', 'd12', 'd13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd21', 'd22', 'd23', 'd24', 'd25',
              'd26', 'd27', 'd28', 'd31', 'd32', 'd33', 'd34', 'd35', 'd36', 'd37', 'd38', 'd41', 'd42', 'd43', 'd44',
              'd45', 'd46', 'd47', 'd48']
    template_name = "prontuario/odontograma_editar.html"
    success_message = "Odontograma Inicial Atualizado com Sucesso!"


def sol_exa_com_detalhes(request, pk=None):
    object = SolicitacaoExamesComplementares.objects.get(pk=pk)
    context = {
        'object': object,
    }
    return render(request, 'prontuario/sol_exa_com_detalhes.html', context)


class SolicitacaoExamesComplementaresUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Solicitação de Exames Complementares'}
    model = SolicitacaoExamesComplementares
    fields = ['sol_exa_com', ]
    template_name = "prontuario/sol_exa_com_editar.html"
    success_message = "Exames Complementares Atualizado com Sucesso!"


def res_exa_com_detalhes(request, pk=None):
    object = ResultadoExamesComplementares.objects.get(pk=pk)
    context = {
        'object': object,

    }
    return render(request, 'prontuario/res_exa_com_detalhes.html', context)


class ResultadoExamesComplementaresUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Resultado de Exames Complementares'}
    model = ResultadoExamesComplementares
    fields = ['res_exa_com', ]
    template_name = "prontuario/res_exa_com_editar.html"


# def pla_tra_i_detalhes(request, pk=None):
#     object = PlanoTratamentoI.objects.get(pk=pk)
#     context = {
#         'object': object,
#     }
#     return render(request, 'prontuario/pla_tra_i_detalhes.html', context)


# class PlanoTratamentoIUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     login_url = reverse_lazy("login")
#     extra_context = {'nome_pagina': 'Plano de Tratamento 1º Opção'}
#     model = PlanoTratamentoI
#     fields = ['plano_tratamento_i', ]
#     template_name = "prontuario/pla_tra_i_editar.html"


# def pla_tra_ii_detalhes(request, pk=None):
#     object = PlanoTratamentoII.objects.get(pk=pk)
#     context = {
#         'object': object,
#     }
#     return render(request, 'prontuario/pla_tra_ii_detalhes.html', context)
#
#
# class PlanoTratamentoIIUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     login_url = reverse_lazy("login")
#     extra_context = {'nome_pagina': 'Plano de Tratamento 2º Opção'}
#     model = PlanoTratamentoI
#     fields = ['plano_tratamento_ii', ]
#     template_name = "prontuario/pla_tra_ii_editar.html"


# def evo_pac_detalhes(request, pk=None):
#     object = EvolucaoPaciente.objects.get(pk=pk)
#     context = {
#         'object': object,
#     }
#     return render(request, 'prontuario/evo_pac_detalhes.html', context)


# class EvolucaoPacienteUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     login_url = reverse_lazy("login")
#     extra_context = {'nome_pagina': 'Evolução do Paciente'}
#     model = EvolucaoPaciente
#     fields = ['evolucao-paciente', ]
#     template_name = "prontuario/evo_pac_editar.html"

@login_required
def odontogramas(request):
    todos_odontogramas = Odontograma.objects.order_by("-id")
    context = {
        "nome_pagina": "Pacientes",
        "todos_odontogramas": todos_odontogramas,

    }
    return render(request, "prontuario/odontogramas.html", context)


@xframe_options_sameorigin
def sup18(request, pk=None):
    # object = Odontograma.objects.get(pk=pk)
    # dente = list(object.dente_17.distal.all())
    # context = {
    #     'dente18': dente,
    # }
    return render(request, "prontuario/Dentes/dentadura-sup-18.html")


@xframe_options_sameorigin
def sup17(request, pk=None):
    object = Odontograma.objects.get(pk=pk)
    dd = list(object.dente_17.distal.all())
    do = list(object.dente_17.oclusal.all())
    dm = list(object.dente_17.mesial.all())
    dl = list(object.dente_17.lingual.all())
    dv = list(object.dente_17.vestibular.all())
    distal = []
    oclusal = []
    mesial = []
    lingual = []
    vestibular = []

    for i in dd:
        i = str(i)
        distal.append(i)
    for i in do:
        i = str(i)
        oclusal.append(i)
    for i in dm:
        i = str(i)
        mesial.append(i)
    for i in dl:
        i = str(i)
        lingual.append(i)
    for i in dv:
        i = str(i)
        vestibular.append(i)
    context = {
        'distal': distal,
        'oclusal': oclusal,
        'mesial': mesial,
        'lingual': lingual,
        'vestibular': vestibular,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-17-detail.html", context)

