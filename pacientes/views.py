import datetime

from _datetime import datetime as dt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from rest_framework import viewsets

from pacientes.forms import PacienteForm, PacienteInfantilForm
from pacientes.models import Paciente, PacienteInfantil, Teste2, Teste
from pacientes.serializers import Teste2Serializer, TesteSerializer
from prontuario.models import *
from usuarios.models import Funcionario
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def paciente_detalhes_geral(request, pk=None):
    instance = Paciente.objects.get(pk=pk)
    prontuario = Prontuario.objects.get(pk=pk)
    anam = Anamnese.objects.get(pk=pk)
    context = {
        'object': instance,
        'prontuario': prontuario,
        'anam': anam,
    }
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
        p = Paciente(nome=nome, nome_social=nome_social, data_nascimento=data_nascimento, sexo_biologico=sexo_biologico,
                     rg=rg, cpf=cpf, raca=raca, estado_civil=estado_civil, grau_instrucao=grau_instrucao,
                     endereco=endereco, cep=cep, bairro=bairro, cidade=cidade, uf=uf, telefone_celular=telefone_celular,
                     informacoes_complementares=informacoes_complementares)
        p.save()

        anamnese = request.POST['anamnese']
        a = Anamnese(anamnese=anamnese)
        a.save()
        messages.success(request, "Paciente atualizado com sucesso")
        return redirect("pacientes")
    return render(request, 'pacientes/paciente_editar3.html', context)


@login_required
def registrar_paciente(request):

    context = {}
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

        if len(Prontuario.objects.all()) == 0:
            numero_prontuario = "1000"
        else:
            numero_prontuario = str(int(Prontuario.objects.all().last().num_prontuario) + 1)
        if len(Paciente.objects.all()) == 0:
            id = 1
        else:
            id = Paciente.objects.all().last().id + 1

        p = Paciente(id=id, nome=nome, nome_social=nome_social, data_nascimento=data_nascimento, sexo_biologico=sexo_biologico,
                     rg=rg, cpf=cpf, raca=raca, estado_civil=estado_civil, grau_instrucao=grau_instrucao,
                     endereco=endereco, cep=cep, bairro=bairro, cidade=cidade, uf=uf, telefone_celular=telefone_celular,
                     informacoes_complementares=informacoes_complementares)

        p.save()
        u = Prontuario(id=id, paciente=p, num_prontuario=numero_prontuario)
        u.save()
        r = Anamnese(id=id, prontuario=u)
        r.save()
        s = InfSaudeSistemica(id=id, prontuario=u)
        s.save()
        t = ExameFisico(id=id, prontuario=u)
        t.save()
        v = SinaisVitaisClinicos(id=id, prontuario=u)
        v.save()
        x = PSR(id=id, prontuario=u)
        x.save()
        # b = Dente(prontuario=u)
        # b.save()
        # y = Odontograma(id=id, prontuario=u)
        # y.save()
        w = SolicitacaoExamesComplementares(id=id, prontuario=u)
        w.save()
        z = ResultadoExamesComplementares(id=id, prontuario=u)
        z.save()

        messages.success(request, "Paciente registrado com sucesso")
        return redirect("pacientes")
    return render(request, "pacientes/paciente_registrar2.html", context)


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
    paginator = Paginator(todos_pacientes, 10)  # Mostra 25 contatos por página
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
    prontuario = Prontuario.objects.get(pk=pk)

    context = {
        "nome_pagina": "INFORMAÇÕES DO PACIENTE",
        'object': instance,
        'prontuario': prontuario,
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

