from _datetime import datetime as dt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from rest_framework import viewsets
from pacientes.forms import PacienteInfantilForm
from pacientes.models import PacienteInfantil, Teste2, Teste
from pacientes.serializers import Teste2Serializer, TesteSerializer
from prontuario.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage

lista_dentes = ['dente_18', 'dente_17', 'dente_16', 'dente_15', 'dente_14', 'dente_13', 'dente_12', 'dente_11',
                'dente_21', 'dente_22', 'dente_23', 'dente_24', 'dente_25', 'dente_26', 'dente_27', 'dente_28',
                'dente_48', 'dente_47', 'dente_46', 'dente_45', 'dente_44', 'dente_43', 'dente_42', 'dente_41',
                'dente_31', 'dente_32', 'dente_33', 'dente_34', 'dente_35', 'dente_36', 'dente_37', 'dente_38',
                ]


@login_required
def registrar_paciente(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        nome_social = request.POST['nome_social']
        data_nascimento = request.POST['data_nascimento']
        sexo_biologico = request.POST['sexo_biologico']
        rg = request.POST['rg']
        cpf = request.POST['cpf']
        raca = request.POST['raca']
        estado_civil = request.POST['estado_civil']
        grau_instrucao = request.POST['grau_instrucao']
        endereco = request.POST['endereco']
        cep = request.POST['cep']
        bairro = request.POST['bairro']
        cidade = request.POST['cidade']
        uf = request.POST['uf']
        telefone_celular = request.POST['telefone_celular']
        informacoes_complementares = request.POST['informacoes_complementares']

        if data_nascimento == "":
            data_nascimento = "2000-01-01"
            data_nascimento = dt.strptime(data_nascimento, '%Y-%m-%d').date()
        else:
            data_nascimento = data_nascimento

        if len(Paciente.objects.all()) == 0:
            numero_prontuario = "1000"
        else:
            numero_prontuario = str(int(Paciente.objects.all().last().prontuario) + 1)
        if len(Paciente.objects.all()) == 0:
            id = 1
        else:
            id = Paciente.objects.all().last().id + 1

        p = Paciente(id=id, nome=nome, nome_social=nome_social, data_nascimento=data_nascimento,
                     sexo_biologico=sexo_biologico,
                     rg=rg, cpf=cpf, raca=raca, estado_civil=estado_civil, grau_instrucao=grau_instrucao,
                     endereco=endereco, cep=cep, bairro=bairro, cidade=cidade, uf=uf, telefone_celular=telefone_celular,
                     informacoes_complementares=informacoes_complementares, prontuario=numero_prontuario)

        p.save()
        # u = Prontuario(id=id, paciente=p, num_prontuario=numero_prontuario)
        # u.save()
        r = Anamnese(id=id, paciente=p, prontuario=numero_prontuario)
        r.save()
        s = InfSaudeSistemica(id=id, paciente=p, prontuario=numero_prontuario)
        s.save()
        t = ExameFisico(id=id, paciente=p, prontuario=numero_prontuario)
        t.save()
        v = SinaisVitaisClinicos(id=id, paciente=p, prontuario=numero_prontuario)
        v.save()
        x = PSR(id=id, paciente=p, prontuario=numero_prontuario)
        x.save()
        w = SolicitacaoExamesComplementares(id=id, paciente=p, prontuario=numero_prontuario)
        w.save()
        # z = ResultadoExamesComplementares(id=id, prontuario=u)
        # z.save()
        d18 = Dente(paciente=p, prontuario=numero_prontuario + '18',  nome='18')
        d18.save()
        d17 = Dente(paciente=p, prontuario=numero_prontuario + '17', nome='17')
        d17.save()
        d16 = Dente(paciente=p, prontuario=numero_prontuario + '16', nome='16')
        d16.save()
        d15 = Dente(paciente=p, prontuario=numero_prontuario + '15', nome='15')
        d15.save()
        d14 = Dente(paciente=p, prontuario=numero_prontuario + '14', nome='14')
        d14.save()
        d13 = Dente(paciente=p, prontuario=numero_prontuario + '13', nome='13')
        d13.save()
        d12 = Dente(paciente=p, prontuario=numero_prontuario + '12', nome='12')
        d12.save()
        d11 = Dente(paciente=p, prontuario=numero_prontuario + '11', nome='11')
        d11.save()

        d21 = Dente(paciente=p, prontuario=numero_prontuario + '21', nome='21')
        d21.save()
        d22 = Dente(paciente=p, prontuario=numero_prontuario + '22', nome='22')
        d22.save()
        d23 = Dente(paciente=p, prontuario=numero_prontuario + '23', nome='23')
        d23.save()
        d24 = Dente(paciente=p, prontuario=numero_prontuario + '24', nome='24')
        d24.save()
        d25 = Dente(paciente=p, prontuario=numero_prontuario + '25', nome='25')
        d25.save()
        d26 = Dente(paciente=p, prontuario=numero_prontuario + '26', nome='26')
        d26.save()
        d27 = Dente(paciente=p, prontuario=numero_prontuario + '27', nome='27')
        d27.save()
        d28 = Dente(paciente=p, prontuario=numero_prontuario + '28', nome='28')
        d28.save()

        d48 = Dente(paciente=p, prontuario=numero_prontuario + '48', nome='48')
        d48.save()
        d47 = Dente(paciente=p, prontuario=numero_prontuario + '47', nome='47')
        d47.save()
        d46 = Dente(paciente=p, prontuario=numero_prontuario + '46', nome='46')
        d46.save()
        d45 = Dente(paciente=p, prontuario=numero_prontuario + '45', nome='45')
        d45.save()
        d44 = Dente(paciente=p, prontuario=numero_prontuario + '44', nome='44')
        d44.save()
        d43 = Dente(paciente=p, prontuario=numero_prontuario + '43', nome='43')
        d43.save()
        d42 = Dente(paciente=p, prontuario=numero_prontuario + '42', nome='42')
        d42.save()
        d41 = Dente(paciente=p, prontuario=numero_prontuario + '41', nome='41')
        d41.save()

        d31 = Dente(paciente=p, prontuario=numero_prontuario + '31', nome='31')
        d31.save()
        d32 = Dente(paciente=p, prontuario=numero_prontuario + '32', nome='32')
        d32.save()
        d33 = Dente(paciente=p, prontuario=numero_prontuario + '33', nome='33')
        d33.save()
        d34 = Dente(paciente=p, prontuario=numero_prontuario + '34', nome='34')
        d34.save()
        d35 = Dente(paciente=p, prontuario=numero_prontuario + '35', nome='35')
        d35.save()
        d36 = Dente(paciente=p, prontuario=numero_prontuario + '36', nome='36')
        d36.save()
        d37 = Dente(paciente=p, prontuario=numero_prontuario + '37', nome='37')
        d37.save()
        d38 = Dente(paciente=p, prontuario=numero_prontuario + '38', nome='38')
        d38.save()

        y = Odontograma(id=id, paciente=p, prontuario=numero_prontuario, dente_18=d18, dente_17=d17, dente_16=d16, dente_15=d15, dente_14=d14,
                        dente_13=d13, dente_12=d12, dente_11=d11, dente_21=d21, dente_22=d22, dente_23=d23,
                        dente_24=d24, dente_25=d25, dente_26=d26, dente_27=d27, dente_28=d28, dente_48=d48,
                        dente_47=d47, dente_46=d46, dente_45=d45, dente_44=d44, dente_43=d43, dente_42=d42,
                        dente_41=d41, dente_31=d31, dente_32=d32, dente_33=d33, dente_34=d34, dente_35=d35,
                        dente_36=d36, dente_37=d37, dente_38=d38)
        y.save()
        messages.success(request, "Paciente registrado com sucesso")
        return redirect("pacientes")
    return render(request, "pacientes/paciente_registrar2.html")


@login_required
def registrar_paciente_inf(request):
    form = PacienteInfantilForm
    if request.method == "POST":
        form = PacienteInfantilForm(request.POST)
        if form.is_valid():
            paciente_inf = form.save(commit=False)
            paciente_inf.save()
            messages.success(request, "Paciente infantil registrado com sucesso")
            return redirect("inicio")
    context = {
        "form": form,
        "messages": messages.success,
    }
    return render(request, "pacientes/paciente_registrar_inf.html", context=context)


@login_required
def pacientes(request):
    todos_pacientes = Paciente.objects.order_by("nome")
    todos_pacientes_inf = PacienteInfantil.objects.order_by("-id")
    paginator = Paginator(todos_pacientes, 25)  # Mostra 25 contatos por página
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        pacientes = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pacientes = paginator.page(paginator.num_pages)
    context = {
        "nome_pagina": "PACIENTES REGISTRADOS",
        "todos_pacientes": todos_pacientes,
        "todos_pacientes_inf": todos_pacientes_inf,
        "pacientes": pacientes,

    }
    return render(request, "pacientes/pacientes.html", context)


def agenda(request):
    context = {
    }
    return render(request, "pacientes/agenda.html", context)


@login_required
def opcoes(request):
    context = {
    }
    return render(request, "pacientes/opcoes.html", context)


@login_required
def paciente_detalhes(request, pk=None):
    instance = Paciente.objects.get(pk=pk)
    # prontuario = Prontuario.objects.get(pk=pk)

    context = {
        "nome_pagina": "INFORMAÇÕES DO PACIENTE",
        'object': instance,
        # 'prontuario': prontuario,
        # 'data_nascimento': data,

    }
    return render(request, 'pacientes/paciente_detalhes2.html', context)


@login_required
def paciente_detalhes_inf(request, pk=None):
    instance = PacienteInfantil.objects.get(pk=pk)
    context = {
        'object': instance
    }
    return render(request, 'pacientes/paciente_detalhes_inf.html', context)


class PacienteUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = Paciente
    fields = ['nome', 'nome_social', 'data_nascimento', 'sexo_biologico', 'rg', 'cpf', 'raca',
              'estado_civil', 'grau_instrucao', 'endereco', 'cep', 'bairro', 'cidade', 'uf',
              'telefone_celular', 'informacoes_complementares']
    # exclude = ('id')
    # template_name = "pacientes/paciente_editar2.html"
    template_name_field = "ATUALIZANDO PACIENTE"
    template_name = "pacientes/paciente_editar2.html"
    success_message = "Paciente atualizado com Sucesso!"

    def data_nasci(self, obj):
        return obj.data_nascimento.strftime("%d/%m/%Y")


class PacienteInfantilUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = PacienteInfantil
    fields = "__all__"
    template_name = "pacientes/paciente_editar_inf.html"
    success_url = reverse_lazy("pacientes")


class PacienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    model = Paciente
    template_name = "pacientes/paciente_delete.html"
    success_url = reverse_lazy("pacientes")


class PacienteInfantilDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    model = PacienteInfantil
    template_name = "pacientes/paciente_delete_inf.html"
    success_url = reverse_lazy("pacientes")


@login_required
def inicio(request, pk=None):
    estenografia_create()
    context = {

    }
    return render(request, "pacientes/inicio.html", context)


@login_required
def registrar_paciente_2(request):
    return render(request, "pacientes/pacientes_menu.html")


class Teste2ViewSet(viewsets.ModelViewSet):
    queryset = Teste2.objects.all()
    serializer_class = Teste2Serializer


class TesteViewSet(viewsets.ModelViewSet):
    queryset = Teste.objects.all()
    serializer_class = TesteSerializer
