from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, QueryDict, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.shortcuts import resolve_url
from prontuario.forms import DenteForm
from prontuario.models import *
from django.views.decorators.clickjacking import xframe_options_sameorigin, xframe_options_deny


def anamnese_detalhes(request, pk=None):
    object = Anamnese.objects.get(pk=pk)
    paciente = Paciente.objects.get(pk=pk)
    inf_sau = InfSaudeSistemica.objects.get(pk=pk)
    context = {
        'anamnese': object,
        'paciente': paciente,
        'inf_sau': inf_sau,
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
    estenografia_create()
    object = Odontograma.objects.get(pk=pk)
    # paciente = Paciente.objects.get(pk=pk)
    dente18 = object.dente_18.pk
    print('dente18 ', dente18)
    dente = list(object.dente_17.distal.all())
    dente2 = []
    for i in dente:
        i = str(i)
        dente2.append(i)
    context = {
        'object': object,
        # 'paciente': paciente,
        'dente': dente2,
        'dente18': dente18,

    }
    return render(request, 'prontuario/odon_detalhes.html', context)


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


# def res_exa_com_detalhes(request, pk=None):
#     object = ResultadoExamesComplementares.objects.get(pk=pk)
#     context = {
#         'object': object,
#
#     }
#     return render(request, 'prontuario/res_exa_com_detalhes.html', context)


# class ResultadoExamesComplementaresUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     login_url = reverse_lazy("login")
#     extra_context = {'nome_pagina': 'Resultado de Exames Complementares'}
#     model = ResultadoExamesComplementares
#     fields = ['res_exa_com', ]
#     template_name = "prontuario/res_exa_com_editar.html"


@xframe_options_sameorigin
def sup18(request, pk=None):
    d18 = Dente.objects.get(pk=pk)
    dente18 = d18.pk
    print(d18)
    dd = list(d18.distal.all())
    do = list(d18.oclusal.all())
    dm = list(d18.mesial.all())
    dl = list(d18.lingual.all())
    dv = list(d18.vestibular.all())

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
        'dente18': dente18,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-18-detail.html", context)


# class DenteUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     login_url = reverse_lazy("login")
#     extra_context = {'nome_pagina': 'Solicitação de Exames Complementares'}
#     model = Dente
#     fields = ['distal', ]
#     template_name = "prontuario/Dentes/dentadura-sup-18-edit.html"
#     success_message = "Dente Atualizado com Sucesso!"


#
@xframe_options_sameorigin
def sup18_edit(request, pk=None):
    dente_18 = Dente.objects.get(pk=pk)
    d18 = dente_18.pk
    print('metodo post')
    print(' !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ', d18)
    estenografia = []
    e1 = Estenografia.objects.get(pk=1)
    e2 = Estenografia.objects.get(pk=2)
    e3 = Estenografia.objects.get(pk=3)
    e4 = Estenografia.objects.get(pk=4)
    e5 = Estenografia.objects.get(pk=5)
    e6 = Estenografia.objects.get(pk=6)
    e7 = Estenografia.objects.get(pk=7)
    e8 = Estenografia.objects.get(pk=8)
    e9 = Estenografia.objects.get(pk=9)
    e10 = Estenografia.objects.get(pk=10)
    e11 = Estenografia.objects.get(pk=11)
    e12 = Estenografia.objects.get(pk=12)
    e13 = Estenografia.objects.get(pk=13)
    e14 = Estenografia.objects.get(pk=14)
    e15 = Estenografia.objects.get(pk=15)
    e16 = Estenografia.objects.get(pk=16)
    e17 = Estenografia.objects.get(pk=17)
    e18 = Estenografia.objects.get(pk=18)
    e19 = Estenografia.objects.get(pk=19)
    e20 = Estenografia.objects.get(pk=20)
    e21 = Estenografia.objects.get(pk=21)
    e22 = Estenografia.objects.get(pk=22)
    e23 = Estenografia.objects.get(pk=23)
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i+1))
        # print(estenografia[i])
        # print(len(estenografia))
    if request.method == 'GET':
        dente_18 = Dente.objects.get(pk=pk)
        d18 = dente_18.pk
        context = {
            'object': d18,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-18-edit.html", context)
    if request.method == 'POST':
        dente_18 = Dente.objects.get(pk=pk)
        print('metodo post')
        print(' !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ', dente_18.pk)
        distal = request.POST.getlist('distal')
        for i in distal:
            if i == '1':
                dente_18.distal.add(e1)
            elif i == '2':
                dente_18.distal.add(e2)
            elif i == '3':
                dente_18.distal.add(e3)
            elif i == '4':
                dente_18.distal.add(e4)
            elif i == '5':
                dente_18.distal.add(e5)
            elif i == '6':
                dente_18.distal.add(e6)
            elif i == '7':
                dente_18.distal.add(e7)
            elif i == '8':
                dente_18.distal.add(e8)
            elif i == '9':
                dente_18.distal.add(e9)
            elif i == '10':
                dente_18.distal.add(e10)
            elif i == '11':
                dente_18.distal.add(e11)
            elif i == '12':
                dente_18.distal.add(e12)
            elif i == '13':
                dente_18.distal.add(e13)
            elif i == '14':
                dente_18.distal.add(e14)
            elif i == '15':
                dente_18.distal.add(e15)
            elif i == '16':
                dente_18.distal.add(e16)
            elif i == '17':
                dente_18.distal.add(e17)
            elif i == '18':
                dente_18.distal.add(e18)
            elif i == '19':
                dente_18.distal.add(e19)
            elif i == '20':
                dente_18.distal.add(e20)
            elif i == '21':
                dente_18.distal.add(e21)
            elif i == '22':
                dente_18.distal.add(e22)
            elif i == '23':
                dente_18.distal.add(e23)

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup18', args=[d18]))
    return render(request, "pacientes/paciente_registrar2.html")


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


@xframe_options_deny
def view_one(request):
    return HttpResponse("I won't display in any frame!")


@xframe_options_sameorigin
def view_two(request):
    return HttpResponse("Display in a frame if it's from the same origin as me.")
