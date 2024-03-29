import random
import time
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
from _datetime import datetime as dt
from .dados import *
from faker import Faker

locales = 'pt-BR'
fake = Faker(locales)
from tqdm import tqdm


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
    odontograma = Odontograma.objects.get(pk=pk)
    context = {
        'odontograma': odontograma,
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


@xframe_options_sameorigin
def sup18_edit(request, pk=None):
    d18 = Dente.objects.get(pk=pk)
    dente18 = d18.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_18 = Dente.objects.get(pk=pk)
        dd = list(dente_18.distal.all())
        do = list(dente_18.oclusal.all())
        dm = list(dente_18.mesial.all())
        dl = list(dente_18.lingual.all())
        dv = list(dente_18.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente18': dente18,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-18-edit.html", context)
    if request.method == 'POST':
        dente_18 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_18.distal.add(estenografia[i])
            else:
                dente_18.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_18.oclusal.add(estenografia[i])
            else:
                dente_18.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_18.mesial.add(estenografia[i])
            else:
                dente_18.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_18.lingual.add(estenografia[i])
            else:
                dente_18.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_18.vestibular.add(estenografia[i])
            else:
                dente_18.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup18', args=[dente18]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup17(request, pk=None):
    d17 = Dente.objects.get(pk=pk)
    dente17 = d17.pk
    print(d17)
    dd = list(d17.distal.all())
    do = list(d17.oclusal.all())
    dm = list(d17.mesial.all())
    dl = list(d17.lingual.all())
    dv = list(d17.vestibular.all())

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
        'dente17': dente17,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-17-detail.html", context)


@xframe_options_sameorigin
def sup17_edit(request, pk=None):
    d17 = Dente.objects.get(pk=pk)
    dente17 = d17.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_17 = Dente.objects.get(pk=pk)
        dd = list(dente_17.distal.all())
        do = list(dente_17.oclusal.all())
        dm = list(dente_17.mesial.all())
        dl = list(dente_17.lingual.all())
        dv = list(dente_17.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente17': dente17,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-18-edit.html", context)
    if request.method == 'POST':
        dente_17 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_17.distal.add(estenografia[i])
            else:
                dente_17.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_17.oclusal.add(estenografia[i])
            else:
                dente_17.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_17.mesial.add(estenografia[i])
            else:
                dente_17.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_17.lingual.add(estenografia[i])
            else:
                dente_17.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_17.vestibular.add(estenografia[i])
            else:
                dente_17.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup17', args=[dente17]))
    return render(request, "pacientes/paciente_registrar2.html")


#
# @xframe_options_deny
# def view_one(request):
#     return HttpResponse("I won't display in any frame!")
#
#
# @xframe_options_sameorigin
# def view_two(request):
#     return HttpResponse("Display in a frame if it's from the same origin as me.")
#
#


def sup16(request, pk=None):
    d16 = Dente.objects.get(pk=pk)
    dente16 = d16.pk
    print(d16)
    dd = list(d16.distal.all())
    do = list(d16.oclusal.all())
    dm = list(d16.mesial.all())
    dl = list(d16.lingual.all())
    dv = list(d16.vestibular.all())

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
        'dente16': dente16,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-16-detail.html", context)


@xframe_options_sameorigin
def sup16_edit(request, pk=None):
    d16 = Dente.objects.get(pk=pk)
    dente16 = d16.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_16 = Dente.objects.get(pk=pk)
        dd = list(dente_16.distal.all())
        do = list(dente_16.oclusal.all())
        dm = list(dente_16.mesial.all())
        dl = list(dente_16.lingual.all())
        dv = list(dente_16.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente16': dente16,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-16-edit.html", context)
    if request.method == 'POST':
        dente_16 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_16.distal.add(estenografia[i])
            else:
                dente_16.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_16.oclusal.add(estenografia[i])
            else:
                dente_16.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_16.mesial.add(estenografia[i])
            else:
                dente_16.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_16.lingual.add(estenografia[i])
            else:
                dente_16.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_16.vestibular.add(estenografia[i])
            else:
                dente_16.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup16', args=[dente16]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup15(request, pk=None):
    d15 = Dente.objects.get(pk=pk)
    dente15 = d15.pk
    print(d15)
    dd = list(d15.distal.all())
    do = list(d15.oclusal.all())
    dm = list(d15.mesial.all())
    dl = list(d15.lingual.all())
    dv = list(d15.vestibular.all())

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
        'dente15': dente15,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-15-detail.html", context)


@xframe_options_sameorigin
def sup15_edit(request, pk=None):
    d15 = Dente.objects.get(pk=pk)
    dente15 = d15.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_15 = Dente.objects.get(pk=pk)
        dd = list(dente_15.distal.all())
        do = list(dente_15.oclusal.all())
        dm = list(dente_15.mesial.all())
        dl = list(dente_15.lingual.all())
        dv = list(dente_15.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente15': dente15,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-15-edit.html", context)
    if request.method == 'POST':
        dente_15 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_15.distal.add(estenografia[i])
            else:
                dente_15.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_15.oclusal.add(estenografia[i])
            else:
                dente_15.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_15.mesial.add(estenografia[i])
            else:
                dente_15.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_15.lingual.add(estenografia[i])
            else:
                dente_15.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_15.vestibular.add(estenografia[i])
            else:
                dente_15.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup15', args=[dente15]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup14(request, pk=None):
    d14 = Dente.objects.get(pk=pk)
    dente14 = d14.pk
    print(d14)
    dd = list(d14.distal.all())
    do = list(d14.oclusal.all())
    dm = list(d14.mesial.all())
    dl = list(d14.lingual.all())
    dv = list(d14.vestibular.all())

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
        'dente14': dente14,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-14-detail.html", context)


@xframe_options_sameorigin
def sup14_edit(request, pk=None):
    d14 = Dente.objects.get(pk=pk)
    dente14 = d14.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_14 = Dente.objects.get(pk=pk)
        dd = list(dente_14.distal.all())
        do = list(dente_14.oclusal.all())
        dm = list(dente_14.mesial.all())
        dl = list(dente_14.lingual.all())
        dv = list(dente_14.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente14': dente14,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-14-edit.html", context)
    if request.method == 'POST':
        dente_14 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_14.distal.add(estenografia[i])
            else:
                dente_14.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_14.oclusal.add(estenografia[i])
            else:
                dente_14.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_14.mesial.add(estenografia[i])
            else:
                dente_14.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_14.lingual.add(estenografia[i])
            else:
                dente_14.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_14.vestibular.add(estenografia[i])
            else:
                dente_14.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup14', args=[dente14]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup13(request, pk=None):
    d13 = Dente.objects.get(pk=pk)
    dente13 = d13.pk
    print(d13)
    dd = list(d13.distal.all())
    do = list(d13.oclusal.all())
    dm = list(d13.mesial.all())
    dl = list(d13.lingual.all())
    dv = list(d13.vestibular.all())

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
        'dente13': dente13,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-13-detail.html", context)


@xframe_options_sameorigin
def sup13_edit(request, pk=None):
    d13 = Dente.objects.get(pk=pk)
    dente13 = d13.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_13 = Dente.objects.get(pk=pk)
        dd = list(dente_13.distal.all())
        do = list(dente_13.oclusal.all())
        dm = list(dente_13.mesial.all())
        dl = list(dente_13.lingual.all())
        dv = list(dente_13.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente13': dente13,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-13-edit.html", context)
    if request.method == 'POST':
        dente_13 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_13.distal.add(estenografia[i])
            else:
                dente_13.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_13.oclusal.add(estenografia[i])
            else:
                dente_13.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_13.mesial.add(estenografia[i])
            else:
                dente_13.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_13.lingual.add(estenografia[i])
            else:
                dente_13.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_13.vestibular.add(estenografia[i])
            else:
                dente_13.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup13', args=[dente13]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup12(request, pk=None):
    d12 = Dente.objects.get(pk=pk)
    dente12 = d12.pk
    print(d12)
    dd = list(d12.distal.all())
    do = list(d12.oclusal.all())
    dm = list(d12.mesial.all())
    dl = list(d12.lingual.all())
    dv = list(d12.vestibular.all())

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
        'dente12': dente12,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-12-detail.html", context)


@xframe_options_sameorigin
def sup12_edit(request, pk=None):
    d12 = Dente.objects.get(pk=pk)
    dente12 = d12.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_12 = Dente.objects.get(pk=pk)
        dd = list(dente_12.distal.all())
        do = list(dente_12.oclusal.all())
        dm = list(dente_12.mesial.all())
        dl = list(dente_12.lingual.all())
        dv = list(dente_12.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente12': dente12,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-12-edit.html", context)
    if request.method == 'POST':
        dente_12 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_12.distal.add(estenografia[i])
            else:
                dente_12.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_12.oclusal.add(estenografia[i])
            else:
                dente_12.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_12.mesial.add(estenografia[i])
            else:
                dente_12.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_12.lingual.add(estenografia[i])
            else:
                dente_12.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_12.vestibular.add(estenografia[i])
            else:
                dente_12.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup12', args=[dente12]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup11(request, pk=None):
    d11 = Dente.objects.get(pk=pk)
    dente11 = d11.pk
    print(d11)
    dd = list(d11.distal.all())
    do = list(d11.oclusal.all())
    dm = list(d11.mesial.all())
    dl = list(d11.lingual.all())
    dv = list(d11.vestibular.all())

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
        'dente11': dente11,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-11-detail.html", context)


@xframe_options_sameorigin
def sup11_edit(request, pk=None):
    d11 = Dente.objects.get(pk=pk)
    dente11 = d11.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_11 = Dente.objects.get(pk=pk)
        dd = list(dente_11.distal.all())
        do = list(dente_11.oclusal.all())
        dm = list(dente_11.mesial.all())
        dl = list(dente_11.lingual.all())
        dv = list(dente_11.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente11': dente11,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-11-edit.html", context)
    if request.method == 'POST':
        dente_11 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_11.distal.add(estenografia[i])
            else:
                dente_11.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_11.oclusal.add(estenografia[i])
            else:
                dente_11.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_11.mesial.add(estenografia[i])
            else:
                dente_11.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_11.lingual.add(estenografia[i])
            else:
                dente_11.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_11.vestibular.add(estenografia[i])
            else:
                dente_11.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup11', args=[dente11]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup21(request, pk=None):
    d21 = Dente.objects.get(pk=pk)
    dente21 = d21.pk
    print(d21)
    dd = list(d21.distal.all())
    do = list(d21.oclusal.all())
    dm = list(d21.mesial.all())
    dl = list(d21.lingual.all())
    dv = list(d21.vestibular.all())

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
        'dente21': dente21,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-21-detail.html", context)


@xframe_options_sameorigin
def sup21_edit(request, pk=None):
    d21 = Dente.objects.get(pk=pk)
    dente21 = d21.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_21 = Dente.objects.get(pk=pk)
        dd = list(dente_21.distal.all())
        do = list(dente_21.oclusal.all())
        dm = list(dente_21.mesial.all())
        dl = list(dente_21.lingual.all())
        dv = list(dente_21.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente21': dente21,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-21-edit.html", context)
    if request.method == 'POST':
        dente_21 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_21.distal.add(estenografia[i])
            else:
                dente_21.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_21.oclusal.add(estenografia[i])
            else:
                dente_21.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_21.mesial.add(estenografia[i])
            else:
                dente_21.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_21.lingual.add(estenografia[i])
            else:
                dente_21.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_21.vestibular.add(estenografia[i])
            else:
                dente_21.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup21', args=[dente21]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup22(request, pk=None):
    d22 = Dente.objects.get(pk=pk)
    dente22 = d22.pk
    print(d22)
    dd = list(d22.distal.all())
    do = list(d22.oclusal.all())
    dm = list(d22.mesial.all())
    dl = list(d22.lingual.all())
    dv = list(d22.vestibular.all())

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
        'dente22': dente22,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-22-detail.html", context)


@xframe_options_sameorigin
def sup22_edit(request, pk=None):
    d22 = Dente.objects.get(pk=pk)
    dente22 = d22.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_22 = Dente.objects.get(pk=pk)
        dd = list(dente_22.distal.all())
        do = list(dente_22.oclusal.all())
        dm = list(dente_22.mesial.all())
        dl = list(dente_22.lingual.all())
        dv = list(dente_22.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente22': dente22,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-22-edit.html", context)
    if request.method == 'POST':
        dente_22 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_22.distal.add(estenografia[i])
            else:
                dente_22.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_22.oclusal.add(estenografia[i])
            else:
                dente_22.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_22.mesial.add(estenografia[i])
            else:
                dente_22.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_22.lingual.add(estenografia[i])
            else:
                dente_22.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_22.vestibular.add(estenografia[i])
            else:
                dente_22.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup22', args=[dente22]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup23(request, pk=None):
    d23 = Dente.objects.get(pk=pk)
    dente23 = d23.pk
    print(d23)
    dd = list(d23.distal.all())
    do = list(d23.oclusal.all())
    dm = list(d23.mesial.all())
    dl = list(d23.lingual.all())
    dv = list(d23.vestibular.all())

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
        'dente23': dente23,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-23-detail.html", context)


@xframe_options_sameorigin
def sup23_edit(request, pk=None):
    d23 = Dente.objects.get(pk=pk)
    dente23 = d23.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_23 = Dente.objects.get(pk=pk)
        dd = list(dente_23.distal.all())
        do = list(dente_23.oclusal.all())
        dm = list(dente_23.mesial.all())
        dl = list(dente_23.lingual.all())
        dv = list(dente_23.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente23': dente23,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-23-edit.html", context)
    if request.method == 'POST':
        dente_23 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_23.distal.add(estenografia[i])
            else:
                dente_23.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_23.oclusal.add(estenografia[i])
            else:
                dente_23.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_23.mesial.add(estenografia[i])
            else:
                dente_23.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_23.lingual.add(estenografia[i])
            else:
                dente_23.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_23.vestibular.add(estenografia[i])
            else:
                dente_23.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup23', args=[dente23]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup24(request, pk=None):
    d24 = Dente.objects.get(pk=pk)
    dente24 = d24.pk
    print(d24)
    dd = list(d24.distal.all())
    do = list(d24.oclusal.all())
    dm = list(d24.mesial.all())
    dl = list(d24.lingual.all())
    dv = list(d24.vestibular.all())

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
        'dente24': dente24,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-24-detail.html", context)


@xframe_options_sameorigin
def sup24_edit(request, pk=None):
    d24 = Dente.objects.get(pk=pk)
    dente24 = d24.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_24 = Dente.objects.get(pk=pk)
        dd = list(dente_24.distal.all())
        do = list(dente_24.oclusal.all())
        dm = list(dente_24.mesial.all())
        dl = list(dente_24.lingual.all())
        dv = list(dente_24.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente24': dente24,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-24-edit.html", context)
    if request.method == 'POST':
        dente_24 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_24.distal.add(estenografia[i])
            else:
                dente_24.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_24.oclusal.add(estenografia[i])
            else:
                dente_24.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_24.mesial.add(estenografia[i])
            else:
                dente_24.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_24.lingual.add(estenografia[i])
            else:
                dente_24.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_24.vestibular.add(estenografia[i])
            else:
                dente_24.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup24', args=[dente24]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup25(request, pk=None):
    d25 = Dente.objects.get(pk=pk)
    dente25 = d25.pk
    print(d25)
    dd = list(d25.distal.all())
    do = list(d25.oclusal.all())
    dm = list(d25.mesial.all())
    dl = list(d25.lingual.all())
    dv = list(d25.vestibular.all())

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
        'dente25': dente25,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-25-detail.html", context)


@xframe_options_sameorigin
def sup25_edit(request, pk=None):
    d25 = Dente.objects.get(pk=pk)
    dente25 = d25.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_25 = Dente.objects.get(pk=pk)
        dd = list(dente_25.distal.all())
        do = list(dente_25.oclusal.all())
        dm = list(dente_25.mesial.all())
        dl = list(dente_25.lingual.all())
        dv = list(dente_25.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente25': dente25,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-25-edit.html", context)
    if request.method == 'POST':
        dente_25 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_25.distal.add(estenografia[i])
            else:
                dente_25.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_25.oclusal.add(estenografia[i])
            else:
                dente_25.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_25.mesial.add(estenografia[i])
            else:
                dente_25.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_25.lingual.add(estenografia[i])
            else:
                dente_25.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_25.vestibular.add(estenografia[i])
            else:
                dente_25.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup25', args=[dente25]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup26(request, pk=None):
    d26 = Dente.objects.get(pk=pk)
    dente26 = d26.pk
    print(d26)
    dd = list(d26.distal.all())
    do = list(d26.oclusal.all())
    dm = list(d26.mesial.all())
    dl = list(d26.lingual.all())
    dv = list(d26.vestibular.all())

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
        'dente26': dente26,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-26-detail.html", context)


@xframe_options_sameorigin
def sup26_edit(request, pk=None):
    d26 = Dente.objects.get(pk=pk)
    dente26 = d26.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_26 = Dente.objects.get(pk=pk)
        dd = list(dente_26.distal.all())
        do = list(dente_26.oclusal.all())
        dm = list(dente_26.mesial.all())
        dl = list(dente_26.lingual.all())
        dv = list(dente_26.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente26': dente26,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-26-edit.html", context)
    if request.method == 'POST':
        dente_26 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_26.distal.add(estenografia[i])
            else:
                dente_26.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_26.oclusal.add(estenografia[i])
            else:
                dente_26.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_26.mesial.add(estenografia[i])
            else:
                dente_26.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_26.lingual.add(estenografia[i])
            else:
                dente_26.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_26.vestibular.add(estenografia[i])
            else:
                dente_26.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup26', args=[dente26]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup27(request, pk=None):
    d27 = Dente.objects.get(pk=pk)
    dente27 = d27.pk
    print(d27)
    dd = list(d27.distal.all())
    do = list(d27.oclusal.all())
    dm = list(d27.mesial.all())
    dl = list(d27.lingual.all())
    dv = list(d27.vestibular.all())

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
        'dente27': dente27,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-27-detail.html", context)


@xframe_options_sameorigin
def sup27_edit(request, pk=None):
    d27 = Dente.objects.get(pk=pk)
    dente27 = d27.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_27 = Dente.objects.get(pk=pk)
        dd = list(dente_27.distal.all())
        do = list(dente_27.oclusal.all())
        dm = list(dente_27.mesial.all())
        dl = list(dente_27.lingual.all())
        dv = list(dente_27.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente27': dente27,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-27-edit.html", context)
    if request.method == 'POST':
        dente_27 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_27.distal.add(estenografia[i])
            else:
                dente_27.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_27.oclusal.add(estenografia[i])
            else:
                dente_27.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_27.mesial.add(estenografia[i])
            else:
                dente_27.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_27.lingual.add(estenografia[i])
            else:
                dente_27.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_27.vestibular.add(estenografia[i])
            else:
                dente_27.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup27', args=[dente27]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup28(request, pk=None):
    d28 = Dente.objects.get(pk=pk)
    dente28 = d28.pk
    print(d28)
    dd = list(d28.distal.all())
    do = list(d28.oclusal.all())
    dm = list(d28.mesial.all())
    dl = list(d28.lingual.all())
    dv = list(d28.vestibular.all())

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
        'dente28': dente28,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-28-detail.html", context)


@xframe_options_sameorigin
def sup28_edit(request, pk=None):
    d28 = Dente.objects.get(pk=pk)
    dente28 = d28.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_28 = Dente.objects.get(pk=pk)
        dd = list(dente_28.distal.all())
        do = list(dente_28.oclusal.all())
        dm = list(dente_28.mesial.all())
        dl = list(dente_28.lingual.all())
        dv = list(dente_28.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente28': dente28,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-28-edit.html", context)
    if request.method == 'POST':
        dente_28 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_28.distal.add(estenografia[i])
            else:
                dente_28.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_28.oclusal.add(estenografia[i])
            else:
                dente_28.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_28.mesial.add(estenografia[i])
            else:
                dente_28.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_28.lingual.add(estenografia[i])
            else:
                dente_28.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_28.vestibular.add(estenografia[i])
            else:
                dente_28.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup28', args=[dente28]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup48(request, pk=None):
    d48 = Dente.objects.get(pk=pk)
    dente48 = d48.pk
    print(d48)
    dd = list(d48.distal.all())
    do = list(d48.oclusal.all())
    dm = list(d48.mesial.all())
    dl = list(d48.lingual.all())
    dv = list(d48.vestibular.all())

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
        'dente48': dente48,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-48-detail.html", context)


@xframe_options_sameorigin
def sup48_edit(request, pk=None):
    d48 = Dente.objects.get(pk=pk)
    dente48 = d48.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_48 = Dente.objects.get(pk=pk)
        dd = list(dente_48.distal.all())
        do = list(dente_48.oclusal.all())
        dm = list(dente_48.mesial.all())
        dl = list(dente_48.lingual.all())
        dv = list(dente_48.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente48': dente48,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-48-edit.html", context)
    if request.method == 'POST':
        dente_48 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_48.distal.add(estenografia[i])
            else:
                dente_48.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_48.oclusal.add(estenografia[i])
            else:
                dente_48.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_48.mesial.add(estenografia[i])
            else:
                dente_48.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_48.lingual.add(estenografia[i])
            else:
                dente_48.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_48.vestibular.add(estenografia[i])
            else:
                dente_48.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup48', args=[dente48]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup47(request, pk=None):
    d47 = Dente.objects.get(pk=pk)
    dente47 = d47.pk
    print(d47)
    dd = list(d47.distal.all())
    do = list(d47.oclusal.all())
    dm = list(d47.mesial.all())
    dl = list(d47.lingual.all())
    dv = list(d47.vestibular.all())

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
        'dente47': dente47,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-47-detail.html", context)


@xframe_options_sameorigin
def sup47_edit(request, pk=None):
    d47 = Dente.objects.get(pk=pk)
    dente47 = d47.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_47 = Dente.objects.get(pk=pk)
        dd = list(dente_47.distal.all())
        do = list(dente_47.oclusal.all())
        dm = list(dente_47.mesial.all())
        dl = list(dente_47.lingual.all())
        dv = list(dente_47.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente47': dente47,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-47-edit.html", context)
    if request.method == 'POST':
        dente_47 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_47.distal.add(estenografia[i])
            else:
                dente_47.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_47.oclusal.add(estenografia[i])
            else:
                dente_47.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_47.mesial.add(estenografia[i])
            else:
                dente_47.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_47.lingual.add(estenografia[i])
            else:
                dente_47.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_47.vestibular.add(estenografia[i])
            else:
                dente_47.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup47', args=[dente47]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup46(request, pk=None):
    d46 = Dente.objects.get(pk=pk)
    dente46 = d46.pk
    print(d46)
    dd = list(d46.distal.all())
    do = list(d46.oclusal.all())
    dm = list(d46.mesial.all())
    dl = list(d46.lingual.all())
    dv = list(d46.vestibular.all())

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
        'dente46': dente46,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-46-detail.html", context)


@xframe_options_sameorigin
def sup46_edit(request, pk=None):
    d46 = Dente.objects.get(pk=pk)
    dente46 = d46.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_46 = Dente.objects.get(pk=pk)
        dd = list(dente_46.distal.all())
        do = list(dente_46.oclusal.all())
        dm = list(dente_46.mesial.all())
        dl = list(dente_46.lingual.all())
        dv = list(dente_46.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente46': dente46,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-46-edit.html", context)
    if request.method == 'POST':
        dente_46 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_46.distal.add(estenografia[i])
            else:
                dente_46.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_46.oclusal.add(estenografia[i])
            else:
                dente_46.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_46.mesial.add(estenografia[i])
            else:
                dente_46.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_46.lingual.add(estenografia[i])
            else:
                dente_46.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_46.vestibular.add(estenografia[i])
            else:
                dente_46.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup46', args=[dente46]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup45(request, pk=None):
    d45 = Dente.objects.get(pk=pk)
    dente45 = d45.pk
    print(d45)
    dd = list(d45.distal.all())
    do = list(d45.oclusal.all())
    dm = list(d45.mesial.all())
    dl = list(d45.lingual.all())
    dv = list(d45.vestibular.all())

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
        'dente45': dente45,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-45-detail.html", context)


@xframe_options_sameorigin
def sup45_edit(request, pk=None):
    d45 = Dente.objects.get(pk=pk)
    dente45 = d45.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_45 = Dente.objects.get(pk=pk)
        dd = list(dente_45.distal.all())
        do = list(dente_45.oclusal.all())
        dm = list(dente_45.mesial.all())
        dl = list(dente_45.lingual.all())
        dv = list(dente_45.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente45': dente45,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-45-edit.html", context)
    if request.method == 'POST':
        dente_45 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_45.distal.add(estenografia[i])
            else:
                dente_45.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_45.oclusal.add(estenografia[i])
            else:
                dente_45.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_45.mesial.add(estenografia[i])
            else:
                dente_45.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_45.lingual.add(estenografia[i])
            else:
                dente_45.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_45.vestibular.add(estenografia[i])
            else:
                dente_45.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup45', args=[dente45]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup44(request, pk=None):
    d44 = Dente.objects.get(pk=pk)
    dente44 = d44.pk
    print(d44)
    dd = list(d44.distal.all())
    do = list(d44.oclusal.all())
    dm = list(d44.mesial.all())
    dl = list(d44.lingual.all())
    dv = list(d44.vestibular.all())

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
        'dente44': dente44,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-44-detail.html", context)


@xframe_options_sameorigin
def sup44_edit(request, pk=None):
    d44 = Dente.objects.get(pk=pk)
    dente44 = d44.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_44 = Dente.objects.get(pk=pk)
        dd = list(dente_44.distal.all())
        do = list(dente_44.oclusal.all())
        dm = list(dente_44.mesial.all())
        dl = list(dente_44.lingual.all())
        dv = list(dente_44.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente44': dente44,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-44-edit.html", context)
    if request.method == 'POST':
        dente_44 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_44.distal.add(estenografia[i])
            else:
                dente_44.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_44.oclusal.add(estenografia[i])
            else:
                dente_44.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_44.mesial.add(estenografia[i])
            else:
                dente_44.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_44.lingual.add(estenografia[i])
            else:
                dente_44.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_44.vestibular.add(estenografia[i])
            else:
                dente_44.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup44', args=[dente44]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup43(request, pk=None):
    d43 = Dente.objects.get(pk=pk)
    dente43 = d43.pk
    print(d43)
    dd = list(d43.distal.all())
    do = list(d43.oclusal.all())
    dm = list(d43.mesial.all())
    dl = list(d43.lingual.all())
    dv = list(d43.vestibular.all())

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
        'dente43': dente43,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-43-detail.html", context)


@xframe_options_sameorigin
def sup43_edit(request, pk=None):
    d43 = Dente.objects.get(pk=pk)
    dente43 = d43.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_43 = Dente.objects.get(pk=pk)
        dd = list(dente_43.distal.all())
        do = list(dente_43.oclusal.all())
        dm = list(dente_43.mesial.all())
        dl = list(dente_43.lingual.all())
        dv = list(dente_43.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente43': dente43,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-43-edit.html", context)
    if request.method == 'POST':
        dente_43 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_43.distal.add(estenografia[i])
            else:
                dente_43.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_43.oclusal.add(estenografia[i])
            else:
                dente_43.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_43.mesial.add(estenografia[i])
            else:
                dente_43.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_43.lingual.add(estenografia[i])
            else:
                dente_43.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_43.vestibular.add(estenografia[i])
            else:
                dente_43.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup43', args=[dente43]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup42(request, pk=None):
    d42 = Dente.objects.get(pk=pk)
    dente42 = d42.pk
    print(d42)
    dd = list(d42.distal.all())
    do = list(d42.oclusal.all())
    dm = list(d42.mesial.all())
    dl = list(d42.lingual.all())
    dv = list(d42.vestibular.all())

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
        'dente42': dente42,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-42-detail.html", context)


@xframe_options_sameorigin
def sup42_edit(request, pk=None):
    d42 = Dente.objects.get(pk=pk)
    dente42 = d42.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_42 = Dente.objects.get(pk=pk)
        dd = list(dente_42.distal.all())
        do = list(dente_42.oclusal.all())
        dm = list(dente_42.mesial.all())
        dl = list(dente_42.lingual.all())
        dv = list(dente_42.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente42': dente42,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-42-edit.html", context)
    if request.method == 'POST':
        dente_42 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_42.distal.add(estenografia[i])
            else:
                dente_42.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_42.oclusal.add(estenografia[i])
            else:
                dente_42.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_42.mesial.add(estenografia[i])
            else:
                dente_42.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_42.lingual.add(estenografia[i])
            else:
                dente_42.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_42.vestibular.add(estenografia[i])
            else:
                dente_42.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup42', args=[dente42]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup41(request, pk=None):
    d41 = Dente.objects.get(pk=pk)
    dente41 = d41.pk
    print(d41)
    dd = list(d41.distal.all())
    do = list(d41.oclusal.all())
    dm = list(d41.mesial.all())
    dl = list(d41.lingual.all())
    dv = list(d41.vestibular.all())

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
        'dente41': dente41,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-41-detail.html", context)


@xframe_options_sameorigin
def sup41_edit(request, pk=None):
    d41 = Dente.objects.get(pk=pk)
    dente41 = d41.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_41 = Dente.objects.get(pk=pk)
        dd = list(dente_41.distal.all())
        do = list(dente_41.oclusal.all())
        dm = list(dente_41.mesial.all())
        dl = list(dente_41.lingual.all())
        dv = list(dente_41.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente41': dente41,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-41-edit.html", context)
    if request.method == 'POST':
        dente_41 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_41.distal.add(estenografia[i])
            else:
                dente_41.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_41.oclusal.add(estenografia[i])
            else:
                dente_41.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_41.mesial.add(estenografia[i])
            else:
                dente_41.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_41.lingual.add(estenografia[i])
            else:
                dente_41.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_41.vestibular.add(estenografia[i])
            else:
                dente_41.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup41', args=[dente41]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup31(request, pk=None):
    d31 = Dente.objects.get(pk=pk)
    dente31 = d31.pk
    print(d31)
    dd = list(d31.distal.all())
    do = list(d31.oclusal.all())
    dm = list(d31.mesial.all())
    dl = list(d31.lingual.all())
    dv = list(d31.vestibular.all())

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
        'dente31': dente31,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-31-detail.html", context)


@xframe_options_sameorigin
def sup31_edit(request, pk=None):
    d31 = Dente.objects.get(pk=pk)
    dente31 = d31.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_31 = Dente.objects.get(pk=pk)
        dd = list(dente_31.distal.all())
        do = list(dente_31.oclusal.all())
        dm = list(dente_31.mesial.all())
        dl = list(dente_31.lingual.all())
        dv = list(dente_31.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente31': dente31,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-31-edit.html", context)
    if request.method == 'POST':
        dente_31 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_31.distal.add(estenografia[i])
            else:
                dente_31.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_31.oclusal.add(estenografia[i])
            else:
                dente_31.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_31.mesial.add(estenografia[i])
            else:
                dente_31.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_31.lingual.add(estenografia[i])
            else:
                dente_31.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_31.vestibular.add(estenografia[i])
            else:
                dente_31.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup31', args=[dente31]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup32(request, pk=None):
    d32 = Dente.objects.get(pk=pk)
    dente32 = d32.pk
    print(d32)
    dd = list(d32.distal.all())
    do = list(d32.oclusal.all())
    dm = list(d32.mesial.all())
    dl = list(d32.lingual.all())
    dv = list(d32.vestibular.all())

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
        'dente32': dente32,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-32-detail.html", context)


@xframe_options_sameorigin
def sup32_edit(request, pk=None):
    d32 = Dente.objects.get(pk=pk)
    dente32 = d32.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_32 = Dente.objects.get(pk=pk)
        dd = list(dente_32.distal.all())
        do = list(dente_32.oclusal.all())
        dm = list(dente_32.mesial.all())
        dl = list(dente_32.lingual.all())
        dv = list(dente_32.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente32': dente32,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-32-edit.html", context)
    if request.method == 'POST':
        dente_32 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_32.distal.add(estenografia[i])
            else:
                dente_32.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_32.oclusal.add(estenografia[i])
            else:
                dente_32.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_32.mesial.add(estenografia[i])
            else:
                dente_32.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_32.lingual.add(estenografia[i])
            else:
                dente_32.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_32.vestibular.add(estenografia[i])
            else:
                dente_32.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup32', args=[dente32]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup33(request, pk=None):
    d33 = Dente.objects.get(pk=pk)
    dente33 = d33.pk
    print(d33)
    dd = list(d33.distal.all())
    do = list(d33.oclusal.all())
    dm = list(d33.mesial.all())
    dl = list(d33.lingual.all())
    dv = list(d33.vestibular.all())

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
        'dente33': dente33,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-33-detail.html", context)


@xframe_options_sameorigin
def sup33_edit(request, pk=None):
    d33 = Dente.objects.get(pk=pk)
    dente33 = d33.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_33 = Dente.objects.get(pk=pk)
        dd = list(dente_33.distal.all())
        do = list(dente_33.oclusal.all())
        dm = list(dente_33.mesial.all())
        dl = list(dente_33.lingual.all())
        dv = list(dente_33.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente33': dente33,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-33-edit.html", context)
    if request.method == 'POST':
        dente_33 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_33.distal.add(estenografia[i])
            else:
                dente_33.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_33.oclusal.add(estenografia[i])
            else:
                dente_33.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_33.mesial.add(estenografia[i])
            else:
                dente_33.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_33.lingual.add(estenografia[i])
            else:
                dente_33.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_33.vestibular.add(estenografia[i])
            else:
                dente_33.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup33', args=[dente33]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup34(request, pk=None):
    d34 = Dente.objects.get(pk=pk)
    dente34 = d34.pk
    print(d34)
    dd = list(d34.distal.all())
    do = list(d34.oclusal.all())
    dm = list(d34.mesial.all())
    dl = list(d34.lingual.all())
    dv = list(d34.vestibular.all())

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
        'dente34': dente34,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-34-detail.html", context)


@xframe_options_sameorigin
def sup34_edit(request, pk=None):
    d34 = Dente.objects.get(pk=pk)
    dente34 = d34.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_34 = Dente.objects.get(pk=pk)
        dd = list(dente_34.distal.all())
        do = list(dente_34.oclusal.all())
        dm = list(dente_34.mesial.all())
        dl = list(dente_34.lingual.all())
        dv = list(dente_34.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente34': dente34,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-34-edit.html", context)
    if request.method == 'POST':
        dente_34 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_34.distal.add(estenografia[i])
            else:
                dente_34.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_34.oclusal.add(estenografia[i])
            else:
                dente_34.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_34.mesial.add(estenografia[i])
            else:
                dente_34.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_34.lingual.add(estenografia[i])
            else:
                dente_34.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_34.vestibular.add(estenografia[i])
            else:
                dente_34.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup34', args=[dente34]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup35(request, pk=None):
    d35 = Dente.objects.get(pk=pk)
    dente35 = d35.pk
    print(d35)
    dd = list(d35.distal.all())
    do = list(d35.oclusal.all())
    dm = list(d35.mesial.all())
    dl = list(d35.lingual.all())
    dv = list(d35.vestibular.all())

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
        'dente35': dente35,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-35-detail.html", context)


@xframe_options_sameorigin
def sup35_edit(request, pk=None):
    d35 = Dente.objects.get(pk=pk)
    dente35 = d35.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_35 = Dente.objects.get(pk=pk)
        dd = list(dente_35.distal.all())
        do = list(dente_35.oclusal.all())
        dm = list(dente_35.mesial.all())
        dl = list(dente_35.lingual.all())
        dv = list(dente_35.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente35': dente35,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-35-edit.html", context)
    if request.method == 'POST':
        dente_35 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_35.distal.add(estenografia[i])
            else:
                dente_35.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_35.oclusal.add(estenografia[i])
            else:
                dente_35.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_35.mesial.add(estenografia[i])
            else:
                dente_35.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_35.lingual.add(estenografia[i])
            else:
                dente_35.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_35.vestibular.add(estenografia[i])
            else:
                dente_35.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup35', args=[dente35]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup36(request, pk=None):
    d36 = Dente.objects.get(pk=pk)
    dente36 = d36.pk
    print(d36)
    dd = list(d36.distal.all())
    do = list(d36.oclusal.all())
    dm = list(d36.mesial.all())
    dl = list(d36.lingual.all())
    dv = list(d36.vestibular.all())

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
        'dente36': dente36,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-36-detail.html", context)


@xframe_options_sameorigin
def sup36_edit(request, pk=None):
    d36 = Dente.objects.get(pk=pk)
    dente36 = d36.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_36 = Dente.objects.get(pk=pk)
        dd = list(dente_36.distal.all())
        do = list(dente_36.oclusal.all())
        dm = list(dente_36.mesial.all())
        dl = list(dente_36.lingual.all())
        dv = list(dente_36.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente36': dente36,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-36-edit.html", context)
    if request.method == 'POST':
        dente_36 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_36.distal.add(estenografia[i])
            else:
                dente_36.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_36.oclusal.add(estenografia[i])
            else:
                dente_36.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_36.mesial.add(estenografia[i])
            else:
                dente_36.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_36.lingual.add(estenografia[i])
            else:
                dente_36.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_36.vestibular.add(estenografia[i])
            else:
                dente_36.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup36', args=[dente36]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup37(request, pk=None):
    d37 = Dente.objects.get(pk=pk)
    dente37 = d37.pk
    print(d37)
    dd = list(d37.distal.all())
    do = list(d37.oclusal.all())
    dm = list(d37.mesial.all())
    dl = list(d37.lingual.all())
    dv = list(d37.vestibular.all())

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
        'dente37': dente37,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-37-detail.html", context)


@xframe_options_sameorigin
def sup37_edit(request, pk=None):
    d37 = Dente.objects.get(pk=pk)
    dente37 = d37.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_37 = Dente.objects.get(pk=pk)
        dd = list(dente_37.distal.all())
        do = list(dente_37.oclusal.all())
        dm = list(dente_37.mesial.all())
        dl = list(dente_37.lingual.all())
        dv = list(dente_37.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente37': dente37,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-37-edit.html", context)
    if request.method == 'POST':
        dente_37 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_37.distal.add(estenografia[i])
            else:
                dente_37.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_37.oclusal.add(estenografia[i])
            else:
                dente_37.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_37.mesial.add(estenografia[i])
            else:
                dente_37.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_37.lingual.add(estenografia[i])
            else:
                dente_37.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_37.vestibular.add(estenografia[i])
            else:
                dente_37.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup37', args=[dente37]))
    return render(request, "pacientes/paciente_registrar2.html")


@xframe_options_sameorigin
def sup38(request, pk=None):
    d38 = Dente.objects.get(pk=pk)
    dente38 = d38.pk
    print(d38)
    dd = list(d38.distal.all())
    do = list(d38.oclusal.all())
    dm = list(d38.mesial.all())
    dl = list(d38.lingual.all())
    dv = list(d38.vestibular.all())

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
        'dente38': dente38,
    }
    return render(request, "prontuario/Dentes/dentadura-sup-38-detail.html", context)


@xframe_options_sameorigin
def sup38_edit(request, pk=None):
    d38 = Dente.objects.get(pk=pk)
    dente38 = d38.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_38 = Dente.objects.get(pk=pk)
        dd = list(dente_38.distal.all())
        do = list(dente_38.oclusal.all())
        dm = list(dente_38.mesial.all())
        dl = list(dente_38.lingual.all())
        dv = list(dente_38.vestibular.all())
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
        print('requisisção GET: ')
        for i in distal:
            print(i)
        context = {
            'dente38': dente38,
            'distal': distal,
            'oclusal': oclusal,
            'mesial': mesial,
            'lingual': lingual,
            'vestibular': vestibular,
        }
        return render(request, "prontuario/Dentes/dentadura-sup-38-edit.html", context)
    if request.method == 'POST':
        dente_38 = Dente.objects.get(pk=pk)
        distal = request.POST.getlist('distal')
        oclusal = request.POST.getlist('oclusal')
        mesial = request.POST.getlist('mesial')
        lingual = request.POST.getlist('lingual')
        vestibular = request.POST.getlist('vestibular')
        for i in range(0, 23):
            if str(i + 1) in distal:
                dente_38.distal.add(estenografia[i])
            else:
                dente_38.distal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in oclusal:
                dente_38.oclusal.add(estenografia[i])
            else:
                dente_38.oclusal.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in mesial:
                dente_38.mesial.add(estenografia[i])
            else:
                dente_38.mesial.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in lingual:
                dente_38.lingual.add(estenografia[i])
            else:
                dente_38.lingual.remove(estenografia[i])
        for i in range(0, 23):
            if str(i + 1) in vestibular:
                dente_38.vestibular.add(estenografia[i])
            else:
                dente_38.vestibular.remove(estenografia[i])

        messages.success(request, "Dente alterado com sucesso")
        return HttpResponsePermanentRedirect(reverse('sup38', args=[dente38]))
    return render(request, "pacientes/paciente_registrar2.html")


def esteografia_random():
    estenografia = []
    for i in range(6):
        esteno = Estenografia.objects.get(pk=random.randint(0, 23))
        estenografia.append(esteno)

    return estenografia


@login_required
def create_data(request):
    if request.method == 'GET':
        atual = len(Paciente.objects.all())
        print(atual)
        context = {
            'atual': atual,
        }
        return render(request, "prontuario/create_data.html", context)

    if request.method == 'POST':
        ini = time.time()
        num = request.POST['qtd']
        qtd = int(num)
        for i in range(1, qtd + 1):
            var = random.randint(0, 1)
            if var == 1:
                nome_fake = fake.name_male() + ' ' + fake.last_name_nonbinary()
                sexo_fake = 'MASCULINO'
            else:
                nome_fake = fake.name_female() + ' ' + fake.last_name_nonbinary()
                sexo_fake = 'FEMININO'

            data_nascimento = fake.date()
            data_nascimento = dt.strptime(data_nascimento, '%Y-%m-%d').date()
            data_nascimento = data_nascimento

            if len(Paciente.objects.all()) == 0:
                numero_prontuario = "1000"
            else:
                numero_prontuario = str(int(Paciente.objects.all().last().prontuario) + 1)
            if len(Paciente.objects.all()) == 0:
                id = 1
            else:
                id = Paciente.objects.all().last().id + 1

            p = Paciente(id=id, nome=nome_fake, data_nascimento=data_nascimento,
                         sexo_biologico=sexo_fake,
                         rg=fake.rg(), cpf=fake.cpf(), raca=raca_random(), estado_civil=estado_civil_random(),
                         grau_instrucao=grau_instruncao_random(),
                         endereco=fake.street_address(), cep=fake.postcode(), bairro=fake.bairro(),
                         cidade=fake.city(), uf=fake.estado()[0], telefone_celular=fake.cellphone_number(),
                         prontuario=numero_prontuario)

            p.save()
            r = Anamnese(id=id, paciente=p, prontuario=numero_prontuario, anamnese=anamnese_random())
            r.save()
            s = InfSaudeSistemica(id=id, paciente=p, prontuario=numero_prontuario,
                                  antecedentes_familiares=antecedentes_familiares_random(),
                                  medicamentos_em_uso=medicamentos_random(), cirurgias_anteriores=cirurgia_random(),
                                  problemas_cardiacos=cardiaco_random(),
                                  problemas_gastrointestinais=gastrointestinais_random(),
                                  alteracoes_sanguineas=alteracoes_sangineas(),
                                  enfermidades_osseas=enfermidades_osseas_random(),
                                  problemas_pulmonares=problemas_pulmonares_random(),
                                  alergias=alegias_random(), habitos=habitos_random()
                                  )
            s.save()
            t = ExameFisico(id=id, paciente=p, prontuario=numero_prontuario,
                            nodulos_linfaticos=nodulos_linfaticos_random(),
                            amigdalas=amigdalas_random(), trigono_retromolar=trigono_retromolar_random(),
                            palato_duro=palato_duro_random(), palato_mole=palato_mole_random(), labios=labios_random(),
                            pele=pele_random(), atm=atm_random(), vestibulo=vestibulo_random(),
                            higiene_bucal=higiene_bucal_random()
                            )
            t.save()
            v = SinaisVitaisClinicos(id=id, paciente=p, prontuario=numero_prontuario,
                                     pressao_arterial=pressao_arterial_random(),
                                     respiracao=respiracao_random(), temperatura=temperatura_random(),
                                     placa_visivel_16v=ipv_random(), placa_visivel_11v=ipv_random(),
                                     placa_visivel_26v=ipv_random(), placa_visivel_36v=ipv_random(),
                                     placa_visivel_31v=ipv_random(), placa_visivel_46v=ipv_random())
            v.save()
            x = PSR(id=id, paciente=p, prontuario=numero_prontuario, sextante_16v=psr_random(),
                    sextante_11v=psr_random(), sextante_26v=psr_random(), sextante_36v=psr_random(),
                    sextante_31v=psr_random(), sextante_46v=psr_random())
            x.save()

            d18 = Dente(paciente=p, prontuario=numero_prontuario, nome='18')
            d18.save()
            for est in range(0, random.randint(1, 7)):
                d18.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d18.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d18.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d18.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d18.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d17 = Dente(paciente=p, prontuario=numero_prontuario, nome='17')
            d17.save()
            for est in range(0, random.randint(1, 7)):
                d17.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d17.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d17.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d17.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d17.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d16 = Dente(paciente=p, prontuario=numero_prontuario, nome='16')
            d16.save()
            for est in range(0, random.randint(1, 7)):
                d16.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d16.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d16.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d16.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d16.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d15 = Dente(paciente=p, prontuario=numero_prontuario, nome='15')
            d15.save()
            for est in range(0, random.randint(1, 7)):
                d15.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d15.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d15.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d15.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d15.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d14 = Dente(paciente=p, prontuario=numero_prontuario, nome='14')
            d14.save()
            for est in range(0, random.randint(1, 7)):
                d14.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d14.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d14.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d14.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d14.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d13 = Dente(paciente=p, prontuario=numero_prontuario, nome='13')
            d13.save()
            for est in range(0, random.randint(1, 7)):
                d13.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d13.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d13.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d13.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d13.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d12 = Dente(paciente=p, prontuario=numero_prontuario, nome='12')
            d12.save()
            for est in range(0, random.randint(1, 7)):
                d12.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d12.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d12.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d12.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d12.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d11 = Dente(paciente=p, prontuario=numero_prontuario, nome='11')
            d11.save()
            for est in range(0, random.randint(1, 7)):
                d11.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d11.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d11.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d11.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d11.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d21 = Dente(paciente=p, prontuario=numero_prontuario, nome='21')
            d21.save()
            for est in range(0, random.randint(1, 7)):
                d21.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d21.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d21.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d21.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d21.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d22 = Dente(paciente=p, prontuario=numero_prontuario, nome='22')
            d22.save()
            for est in range(0, random.randint(1, 7)):
                d22.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d22.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d22.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d22.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d22.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d23 = Dente(paciente=p, prontuario=numero_prontuario, nome='23')
            d23.save()
            for est in range(0, random.randint(1, 7)):
                d23.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d23.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d23.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d23.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d23.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d24 = Dente(paciente=p, prontuario=numero_prontuario, nome='24')
            d24.save()
            for est in range(0, random.randint(1, 7)):
                d24.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d24.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d24.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d24.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d24.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d25 = Dente(paciente=p, prontuario=numero_prontuario, nome='25')
            d25.save()
            for est in range(0, random.randint(1, 7)):
                d25.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d25.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d25.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d25.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d25.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d26 = Dente(paciente=p, prontuario=numero_prontuario, nome='26')
            d26.save()
            for est in range(0, random.randint(1, 7)):
                d26.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d26.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d26.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d26.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d26.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d27 = Dente(paciente=p, prontuario=numero_prontuario, nome='27')
            d27.save()
            for est in range(0, random.randint(1, 7)):
                d27.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d27.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d27.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d27.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d27.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d28 = Dente(paciente=p, prontuario=numero_prontuario, nome='28')
            d28.save()
            for est in range(0, random.randint(1, 7)):
                d28.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d28.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d28.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d28.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d28.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d48 = Dente(paciente=p, prontuario=numero_prontuario, nome='48')
            d48.save()
            for est in range(0, random.randint(1, 7)):
                d48.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d48.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d48.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d48.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d48.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            d47 = Dente(paciente=p, prontuario=numero_prontuario, nome='47')
            d47.save()
            for est in range(0, random.randint(1, 7)):
                d47.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d47.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d47.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d47.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d47.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d46 = Dente(paciente=p, prontuario=numero_prontuario, nome='46')
            d46.save()
            for est in range(0, random.randint(1, 7)):
                d46.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d46.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d46.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d46.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d46.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            d45 = Dente(paciente=p, prontuario=numero_prontuario, nome='45')
            d45.save()
            for est in range(0, random.randint(1, 7)):
                d45.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d45.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d45.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d45.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d45.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d44 = Dente(paciente=p, prontuario=numero_prontuario, nome='44')
            d44.save()
            for est in range(0, random.randint(1, 7)):
                d44.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d44.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d44.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d44.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d44.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d43 = Dente(paciente=p, prontuario=numero_prontuario, nome='43')
            d43.save()
            for est in range(0, random.randint(1, 7)):
                d43.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d43.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d43.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d43.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d43.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d42 = Dente(paciente=p, prontuario=numero_prontuario, nome='42')
            d42.save()
            for est in range(0, random.randint(1, 7)):
                d42.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d42.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d42.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d42.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d42.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d41 = Dente(paciente=p, prontuario=numero_prontuario, nome='41')
            d41.save()
            for est in range(0, random.randint(1, 7)):
                d41.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d41.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d41.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d41.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d41.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d31 = Dente(paciente=p, prontuario=numero_prontuario, nome='31')
            d31.save()
            for est in range(0, random.randint(1, 7)):
                d31.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d31.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d31.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d31.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d31.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d32 = Dente(paciente=p, prontuario=numero_prontuario, nome='32')
            d32.save()
            for est in range(0, random.randint(1, 7)):
                d32.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d32.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d32.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d32.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d32.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d33 = Dente(paciente=p, prontuario=numero_prontuario, nome='33')
            d33.save()
            for est in range(0, random.randint(1, 7)):
                d33.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d33.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d33.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d33.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d33.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d34 = Dente(paciente=p, prontuario=numero_prontuario, nome='34')
            d34.save()
            for est in range(0, random.randint(1, 7)):
                d34.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d34.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d34.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d34.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d34.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d35 = Dente(paciente=p, prontuario=numero_prontuario, nome='35')
            d35.save()
            for est in range(0, random.randint(1, 7)):
                d35.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d35.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d35.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d35.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d35.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d36 = Dente(paciente=p, prontuario=numero_prontuario, nome='36')
            d36.save()
            for est in range(0, random.randint(1, 7)):
                d36.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d36.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d36.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d36.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d36.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d37 = Dente(paciente=p, prontuario=numero_prontuario, nome='37')
            d37.save()
            for est in range(0, random.randint(1, 7)):
                d37.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d37.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d37.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d37.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d37.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            d38 = Dente(paciente=p, prontuario=numero_prontuario, nome='38')
            d38.save()
            for est in range(0, random.randint(1, 7)):
                d38.distal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d38.oclusal.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d38.mesial.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d38.lingual.add(Estenografia.objects.get(pk=random.randint(1, 23)))
            for est in range(0, random.randint(1, 7)):
                d38.vestibular.add(Estenografia.objects.get(pk=random.randint(1, 23)))

            y = Odontograma(id=id, paciente=p, prontuario=numero_prontuario, dente_18=d18, dente_17=d17, dente_16=d16,
                            dente_15=d15, dente_14=d14,
                            dente_13=d13, dente_12=d12, dente_11=d11, dente_21=d21, dente_22=d22, dente_23=d23,
                            dente_24=d24, dente_25=d25, dente_26=d26, dente_27=d27, dente_28=d28, dente_48=d48,
                            dente_47=d47, dente_46=d46, dente_45=d45, dente_44=d44, dente_43=d43, dente_42=d42,
                            dente_41=d41, dente_31=d31, dente_32=d32, dente_33=d33, dente_34=d34, dente_35=d35,
                            dente_36=d36, dente_37=d37, dente_38=d38)
            y.save()
            with tqdm(total=qtd) as barra_progresso:
                barra_progresso.update(i)
        fim = time.time()
        tempo = (fim - ini)
        print(f'TEMPO: {tempo:.2f} SEGUNDOS ')
        messages.success(request, "Pacientes Criados com Sucesso!")
        return redirect("create_data")
    return render(request, "prontuario/create_data.html")
