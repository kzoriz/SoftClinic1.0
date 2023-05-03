import random

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
    dente_18 = Dente.objects.get(pk=pk)
    d18 = dente_18.pk
    estenografia = []
    for i in range(23):
        estenografia.append(Estenografia.objects.get(pk=i + 1))
    if request.method == 'GET':
        dente_18 = Dente.objects.get(pk=pk)
        d18 = dente_18.pk
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
            'object': d18,
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
        return HttpResponsePermanentRedirect(reverse('sup18', args=[d18]))
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


@xframe_options_deny
def view_one(request):
    return HttpResponse("I won't display in any frame!")


@xframe_options_sameorigin
def view_two(request):
    return HttpResponse("Display in a frame if it's from the same origin as me.")


def request_date(request, dado):
    context = {
        'dado': dado,
    }
    return render(request, "prontuario/create_data.html", context)


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
        messages.success(request, "Pacientes Criados com Sucesso!")
        return redirect("create_data")
    return render(request, "prontuario/create_data.html")
