import datetime
import string
from _datetime import datetime as dt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from rest_framework import viewsets
from pacientes.forms import PacienteInfantilForm
from pacientes.models import PacienteInfantil, Teste2, Teste
from pacientes.serializers import Teste2Serializer, TesteSerializer
from prontuario.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Max, Min
from datetime import datetime
from django.db.models import Q


def calcular_idade(data_nascimento):
    data_atual = datetime.now()
    idade = data_atual.year - data_nascimento.year - (
                (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    return idade


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
        d18 = Dente(paciente=p, prontuario=numero_prontuario + '18', nome='18')
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

        y = Odontograma(id=id, paciente=p, prontuario=numero_prontuario, dente_18=d18, dente_17=d17, dente_16=d16,
                        dente_15=d15, dente_14=d14,
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


@login_required
def filtros(request):
    opcao = request.GET.get('opcao')
    entrada = request.GET.get('entrada')
    qtd1 = 0
    qtd2 = Paciente.objects.all().count()
    percent = qtd1 / qtd2
    dente = Dente.objects.all()
    most_common_variavel_value = " "
    if opcao == 'opcao1':
        #todos_pacientes = Paciente.objects.all().filter(sexo_biologico="MASCULINO")
        masculino = Paciente.objects.all().filter(sexo_biologico="MASCULINO")
        feminino = Paciente.objects.all().filter(sexo_biologico="FEMININO")

        #qtd1 = todos_pacientes.count()
        qtd1 = masculino.count()
        qtd2 = feminino.count()
        total = Paciente.objects.all().count()
        percent = (qtd1*100 / total)
        print(qtd1, qtd2, percent)
        most_common_variavel = Paciente.objects.values('sexo_biologico').annotate(
            count=Count('sexo_biologico')).order_by(
            '-count').first()
        # print(most_common_variavel.count())
        if most_common_variavel:
            most_common_variavel_value = most_common_variavel['sexo_biologico']
        else:
            most_common_variavel_value = None
        opcao = 'opcao1'
        context = {
            "nome_pagina": "PACIENTES REGISTRADOS",
            "todos_pacientes": masculino,
            #"pacientes": pacientes,
            "qtd1": qtd1,
            "qtd2": qtd2,
            "total": total,
            "percent": percent,
            "opcao": opcao,
            "entrada": entrada,
            'most_common_variavel': most_common_variavel_value,

        }
        return render(request, "pacientes/filtros.html", context)
    elif opcao == 'opcao2':
        todos_pacientes = Paciente.objects.all().filter(sexo_biologico="FEMININO")
        qtd1 = todos_pacientes.count()
        qtd2 = Paciente.objects.all().count()
        percent = (qtd1 / qtd2) * 100
        print(qtd1, qtd2, percent)
        most_common_variavel = Paciente.objects.values('sexo_biologico').annotate(
            count=Count('sexo_biologico')).order_by(
            '-count').first()
        # print(most_common_variavel.count())
        if most_common_variavel:
            most_common_variavel_value = most_common_variavel['sexo_biologico']
        else:
            most_common_variavel_value = None
        opcao = 'SEXO BIOLOGICO'
        data_limite = '2023-08-31'
        data_maxima = Paciente.objects.filter(data_nascimento__lt=data_limite).aggregate(Max('data_nascimento'))[
            'data_nascimento__max']
        data_minima = Paciente.objects.filter(data_nascimento__lt=data_limite).aggregate(Min('data_nascimento'))[
            'data_nascimento__min']

        print("idade minima: ", calcular_idade(data_maxima))
        print("idade maxima: ", calcular_idade(data_minima))

    elif opcao == 'opcao3':
        todos_pacientes = Paciente.objects.all().filter(raca=entrada.upper())
        qtd1 = todos_pacientes.count()
        qtd2 = Paciente.objects.all().count()
        percent = (qtd1 / qtd2) * 100
        print(qtd1, qtd2, percent)
        most_common_variavel = Paciente.objects.values('raca').annotate(count=Count('raca')).order_by('-count').first()
        # print(most_common_variavel.count())
        if most_common_variavel:
            most_common_variavel_value = most_common_variavel['raca']
        else:
            most_common_variavel_value = None
    elif opcao == 'opcao4':
        todos_pacientes = Paciente.objects.all().filter(grau_instrucao=entrada.upper())
        qtd1 = todos_pacientes.count()
        qtd2 = Paciente.objects.all().count()
        percent = (qtd1 / qtd2) * 100
        print(qtd1, qtd2, percent)
        most_common_variavel = Paciente.objects.values('grau_instrucao').annotate(
            count=Count('grau_instrucao')).order_by('-count').first()
        # print(most_common_variavel.count())
        if most_common_variavel:
            most_common_variavel_value = most_common_variavel['grau_instrucao']
        else:
            most_common_variavel_value = None
    elif opcao == 'opcao5':
        most_common_variavel = Paciente.objects.values('cidade').annotate(count=Count('cidade')).order_by(
            '-count').first()
        # print(most_common_variavel.count())
        if most_common_variavel:
            most_common_variavel_value = most_common_variavel['cidade']
            print(most_common_variavel_value)
        else:
            most_common_variavel_value = None
        todos_pacientes = Paciente.objects.all().filter(cidade=most_common_variavel_value)
    elif opcao == 'opcao6':
        todos_pacientes = Paciente.objects.all().filter(sexo_biologico='FEMININO')

    elif opcao == 'opcao7':
        #todos_pacientes = Paciente.objects.all().filter(sexo_biologico="FEMININO")

        #DADOS FEMININO
        pacientes_femininos = Dente.objects.filter(Q(distal__nome__icontains='lesao de carie primaria')
                                               | Q(mesial__nome__icontains='lesao de carie primaria')
                                               | Q(oclusal__nome__icontains='lesao de carie primaria')
                                               | Q(lingual__nome__icontains='lesao de carie primaria')
                                               | Q(vestibular__nome__icontains='lesao de carie primaria'),
                                                paciente__sexo_biologico__icontains='feminino',
                                                nome='18')
        pacientes_femininos = pacientes_femininos.distinct()

        qtd_fem_s = pacientes_femininos.count()
        qtd_fem_total = Paciente.objects.filter(sexo_biologico='FEMININO').count()
        #print("opção 7\n")
        qtd_fem_n = qtd_fem_total - qtd_fem_s
        #print(qtd_fem_s, qtd_fem_total)
        percentual = (qtd_fem_s / qtd_fem_total) * 100
        percent_fem_s = "{:.1f}".format(percentual)
        #print("percent ")
        #print(percent_fem_s)

        #DADOS MASCULINO

        pacientes_masculinos = Dente.objects.filter(Q(distal__nome__icontains='lesao de carie primaria')
                                                   | Q(mesial__nome__icontains='lesao de carie primaria')
                                                   | Q(oclusal__nome__icontains='lesao de carie primaria')
                                                   | Q(lingual__nome__icontains='lesao de carie primaria')
                                                   | Q(vestibular__nome__icontains='lesao de carie primaria'),
                                                   paciente__sexo_biologico__icontains='MASCULINO',
                                                   nome='18')
        pacientes_masculinos = pacientes_masculinos.distinct()
        qtd_masc_s = pacientes_masculinos.count()
        qtd_masc_total = Paciente.objects.filter(sexo_biologico='MASCULINO').count()
        qtd_masc_n = qtd_masc_total - qtd_masc_s
        percentual_masc = (qtd_masc_s / qtd_masc_total) * 100
        percent_masc_s = "{:.1f}".format(percentual_masc)

        # MAIOR OCORRENCIA
        most_common_variavel = Paciente.objects.values('sexo_biologico').annotate(
            count=Count('sexo_biologico')).order_by(
            '-count').first()
        # print(most_common_variavel.count())
        if most_common_variavel:
            most_common_variavel_value = most_common_variavel['sexo_biologico']
        else:
            most_common_variavel_value = None

        #FAIXA ETARIA FEMININA

        data_atual = datetime.today()
        data_formatada = data_atual.strftime('%Y-%m-%d')
        data_limite = data_formatada
        data_maxima = pacientes_femininos.filter(paciente__data_nascimento__lt=data_limite).aggregate(Max('paciente__data_nascimento'))[
            'paciente__data_nascimento__max']
        data_minima = Paciente.objects.filter(data_nascimento__lt=data_limite).aggregate(Min('data_nascimento'))[
            'data_nascimento__min']
        print(data_maxima)
        datas_fem = [paciente.paciente.data_nascimento for paciente in pacientes_femininos]
        print(datas_fem, type(datas_fem[0]))
        jovem_fem = []
        adulto_fem = []
        idoso_fem = []
        for i in range(len(pacientes_femininos)):
            #data_string = datas[i].strftime("%Y-%m-%d")
            idade = calcular_idade(datas_fem[i])
            if idade < 20:
                jovem_fem.append(idade)
            elif 20 <= idade < 60:
                adulto_fem.append(idade)
            else:
                idoso_fem.append(idade)
        print(len(jovem_fem), len(adulto_fem),  len(idoso_fem))
        #print(data_string)
        print("idade minima: ", calcular_idade(data_maxima))
        print("idade maxima: ", calcular_idade(data_minima))

        #RAÇA FEMININA
        racas_fem = [paciente.paciente.raca for paciente in pacientes_femininos]
        amarelo_fem = []
        indigena_fem = []
        branco_fem = []
        pardo_fem = []
        ndn_fem = []
        for i in range(len(racas_fem)):

            if racas_fem[i] =='AMARELO':
                amarelo_fem.append(racas_fem[i])
            elif racas_fem[i] == 'INDIGENA':
                indigena_fem.append(racas_fem[i])
            elif racas_fem[i] == 'BRANCO':
                branco_fem.append(racas_fem[i])
            elif racas_fem[i] == 'PARDO':
                pardo_fem.append(racas_fem[i])
            else:
                ndn_fem.append(racas_fem[i])
        print("raças femininas", amarelo_fem, indigena_fem, branco_fem, pardo_fem, ndn_fem)

        #ESTADO CIVIL FEMININO

        estado_civil_fem = [paciente.paciente.estado_civil for paciente in pacientes_femininos]
        casado_fem = []
        solteiro_fem = []
        divorciado_fem = []
        viuvo_fem = []
        separado_fem = []
        ec_ndn_fem = []
        print("estado civil feminino",estado_civil_fem)
        for i in range(len(estado_civil_fem)):
            if estado_civil_fem[i] =='SEPARADO(A)':
                separado_fem.append(estado_civil_fem[i])
            elif estado_civil_fem[i] == 'DIVORCIADO(A)':
                divorciado_fem.append(estado_civil_fem[i])
            elif estado_civil_fem[i] == 'CASADO(A)':
                casado_fem.append(estado_civil_fem[i])
            elif estado_civil_fem[i] == 'SOLTEIRO(A)':
                solteiro_fem.append(estado_civil_fem[i])
            elif estado_civil_fem[i] == 'VIUVO(A)':
                viuvo_fem.append(estado_civil_fem[i])
            else:
                ec_ndn_fem.append(estado_civil_fem[i])

        print("estado civil fem**", separado_fem, solteiro_fem, casado_fem, viuvo_fem, divorciado_fem, ec_ndn_fem)

        #CIDADES FEMININO

        cidades_fem = [paciente.paciente.cidade for paciente in pacientes_femininos]
        cidades_fem.append('Cardoso Alegre')
        print("cidades fem ",cidades_fem)
        # Converter para um conjunto (set) para remover duplicados
        cidades_fem_set = set(cidades_fem)

        # Converter de volta para uma lista
        cidades_fem_lista = list(cidades_fem_set)

        print(" lista sem duplicatas cidades fem", cidades_fem_lista, type(cidades_fem_lista))
        ocorrencias_cidades_fem = []
        for i in range(len(cidades_fem_lista)):
            ocorrencias_fem = cidades_fem.count(cidades_fem_lista[i])
            ocorrencias_cidades_fem.append(ocorrencias_fem)
        print("ocorrencia cidades fem ", ocorrencias_cidades_fem)
        cidades_fem_lista_str = str(cidades_fem_lista)
        ocorrencias_cidades_fem_str = str(ocorrencias_cidades_fem)
        print(cidades_fem_lista_str, type(cidades_fem_lista_str))
        print(ocorrencias_cidades_fem_str, type(ocorrencias_cidades_fem_str))

        valores = [10, 20, 30, 40]
        rotulos = ['Categoria 1', 'Categoria 2', 'Categoria 3','Categoria 4']

        #GRAU INSTRUÇÃO FEMININA

        grau_instrucao_fem = [paciente.paciente.grau_instrucao for paciente in pacientes_femininos]
        analfabeto_fem = []
        q5_incompleto_fem = []
        q5_completo_fem = []
        s6_9_fundamental_fem = []
        fundamental_completo_fem = []
        medio_incompleto_fem = []
        medio_completo_fem = []
        superior_incompleto_fem = []
        superior_completo_fem = []
        mestrado_fem = []
        doutorado_fem = []
        gi_ndn_fem = []
        print("estado GRAU INSTRUÇÃO feminino", grau_instrucao_fem)
        for i in range(len(grau_instrucao_fem)):
            if grau_instrucao_fem[i] =='ANALFABETO':
                analfabeto_fem.append(grau_instrucao_fem[i])
            elif grau_instrucao_fem[i] == '5º ANO INCOMPLETO':
                q5_incompleto_fem.append(grau_instrucao_fem[i])
            elif grau_instrucao_fem[i] == '5º ANO COMPLETO':
                q5_completo_fem.append(grau_instrucao_fem[i])
            elif grau_instrucao_fem[i] == 'FUNDAMENTAL INCOMPLETO':
                s6_9_fundamental_fem.append(grau_instrucao_fem[i])
            elif grau_instrucao_fem[i] == 'FUNDAMENTAL COMPLETO':
                fundamental_completo_fem.append(grau_instrucao_fem[i])
            elif grau_instrucao_fem[i] == 'MEDIO INCOMPLETO':
                medio_incompleto_fem.append(grau_instrucao_fem[i])
            elif grau_instrucao_fem[i] == 'MEDIO COMPLETO':
                medio_completo_fem.append(grau_instrucao_fem[i])
            elif grau_instrucao_fem[i] == 'SUPERIOR INCOMPLETO':
                superior_incompleto_fem.append(grau_instrucao_fem[i])
            elif grau_instrucao_fem[i] == 'SUPERIOR COMPLETO':
                superior_completo_fem.append(grau_instrucao_fem[i])
            elif grau_instrucao_fem[i] == 'MESTRADO':
                mestrado_fem.append(grau_instrucao_fem[i])
            elif grau_instrucao_fem[i] == 'DOUTORADO':
                doutorado_fem.append(grau_instrucao_fem[i])
            else:
                gi_ndn_fem.append(grau_instrucao_fem[i])

        print("grau intrução fem**",
            analfabeto_fem,
            q5_incompleto_fem,
            q5_completo_fem,
            s6_9_fundamental_fem,
            fundamental_completo_fem,
            medio_incompleto_fem,
            medio_completo_fem,
            superior_incompleto_fem,
            superior_completo_fem,
            mestrado_fem ,
            doutorado_fem,
            gi_ndn_fem,
            )






        #FAIXA ETARIA MASCULINA

        # data_atual = datetime.today()
        # data_formatada = data_atual.strftime('%Y-%m-%d')
        # data_limite = data_formatada
        # data_maxima = pacientes_masculinos.filter(paciente__data_nascimento__lt=data_limite).aggregate(
        #     Max('paciente__data_nascimento'))[
        #     'paciente__data_nascimento__max']
        # data_minima = Paciente.objects.filter(data_nascimento__lt=data_limite).aggregate(Min('data_nascimento'))[
        #     'data_nascimento__min']
        # print(data_maxima)
        datas_masc = [paciente.paciente.data_nascimento for paciente in pacientes_masculinos]
        print(datas_masc, type(datas_masc[0]))
        jovem_masc = []
        adulto_masc = []
        idoso_masc = []
        for i in range(len(pacientes_masculinos)):
            # data_string = datas[i].strftime("%Y-%m-%d")
            idade = calcular_idade(datas_masc[i])
            if idade < 20:
                jovem_masc.append(idade)
            elif 20 <= idade < 60:
                adulto_masc.append(idade)
            else:
                idoso_masc.append(idade)
        print(len(jovem_masc), len(adulto_masc), len(idoso_masc))
        # print(data_string)
        print("idade minima: ", calcular_idade(data_maxima))
        print("idade maxima: ", calcular_idade(data_minima))

        # RAÇA MASCULINO
        racas_masc = [paciente.paciente.raca for paciente in pacientes_masculinos]
        amarelo_masc = []
        indigena_masc = []
        branco_masc = []
        pardo_masc = []
        ndn_masc = []
        for i in range(len(racas_masc)):

            if racas_masc[i] == 'AMARELO':
                amarelo_masc.append(racas_masc[i])
            elif racas_masc[i] == 'INDIGENA':
                indigena_masc.append(racas_masc[i])
            elif racas_masc[i] == 'BRANCO':
                branco_masc.append(racas_masc[i])
            elif racas_masc[i] == 'PARDO':
                pardo_masc.append(racas_masc[i])
            else:
                ndn_masc.append(racas_masc[i])
        print("raças masculino", amarelo_masc, indigena_masc, branco_masc, pardo_masc, ndn_masc)

        #ESTADO CIVIL MASCULINO

        estado_civil_masc = [paciente.paciente.estado_civil for paciente in pacientes_masculinos]
        casado_masc = []
        solteiro_masc = []
        divorciado_masc = []
        viuvo_masc = []
        separado_masc = []
        ec_ndn_masc = []
        print("estado civil masculino",estado_civil_masc)
        for i in range(len(estado_civil_masc)):
            if estado_civil_masc[i] =='SEPARADO(A)':
                separado_masc.append(estado_civil_masc[i])
            elif estado_civil_masc[i] == 'DIVORCIADO(A)':
                divorciado_masc.append(estado_civil_masc[i])
            elif estado_civil_masc[i] == 'CASADO(A)':
                casado_masc.append(estado_civil_masc[i])
            elif estado_civil_masc[i] == 'SOLTEIRO(A)':
                solteiro_masc.append(estado_civil_masc[i])
            elif estado_civil_masc[i] == 'VIUVO(A)':
                viuvo_masc.append(estado_civil_masc[i])
            else:
                ec_ndn_masc.append(estado_civil_masc[i])

        print("estado civil masc**", separado_masc, solteiro_masc, casado_masc, viuvo_masc, divorciado_masc, ec_ndn_masc)

        opcao = 'opcao7'
        paginator = Paginator(pacientes_femininos, 25)  # Mostra 25 contatos por página
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
            #"todos_pacientes": todos_pacientes,
            "pacientes": pacientes,
            "qtd_fem_s": qtd_fem_s,
            "qtd_fem_n": qtd_fem_n,
            "percent_fem": percent_fem_s,
            "qtd_masc_s": qtd_masc_s,
            "qtd_masc_n": qtd_masc_n,
            "percent_masc": percent_masc_s,

            "jovem_fem": len(jovem_fem),
            "adulto_fem": len(adulto_fem),
            "idoso_fem": len(idoso_fem),

            "amarelo_fem": len(amarelo_fem),
            "branco_fem": len(branco_fem),
            "pardo_fem": len(pardo_fem),
            "indigena_fem": len(indigena_fem),
            "ndn_fem": len(ndn_fem),

            "soteiro_fem": len(solteiro_fem),
            "casado_fem": len(casado_fem),
            "divorciado_fem": len(divorciado_fem),
            "viuvo_fem": len(viuvo_fem),
            "separado_fem": len(separado_fem),
            "ec_ndn_fem": len(ec_ndn_fem),

            "cidades_fem": cidades_fem_lista,
            "ocorrencias_fem": ocorrencias_cidades_fem,
            'dados_grafico': valores,
            'labels_grafico': rotulos,

            'analfabeto_fem': len(analfabeto_fem),
            'q5_incompleto_fem': len(q5_incompleto_fem),
            'q5_completo_fem': len(q5_completo_fem),
            's6_9_fundamental_fem': len(s6_9_fundamental_fem),
            'fundamental_completo_fem': len(fundamental_completo_fem),
            'medio_incompleto_fem': len(medio_incompleto_fem),
            'medio_completo_fem': len(medio_completo_fem),
            'superior_incompleto_fem': len(superior_incompleto_fem),
            'superior_completo_fem': len(superior_completo_fem),
            'mestrado_fem': len(mestrado_fem),
            'doutorado_fem': len(doutorado_fem),
            'gi_ndn_fem': len(gi_ndn_fem),

            "jovem_masc": len(jovem_masc),
            "adulto_masc": len(adulto_masc),
            "idoso_masc": len(idoso_masc),

            "amarelo_masc": len(amarelo_masc),
            "branco_masc": len(branco_masc),
            "pardo_masc": len(pardo_masc),
            "indigena_masc": len(indigena_masc),
            "ndn_masc": len(ndn_masc),

            "solteiro_masc": len(solteiro_masc),
            "casado_masc": len(casado_masc),
            "divorciado_masc": len(divorciado_masc),
            "viuvo_masc": len(viuvo_masc),
            "separado_masc": len(separado_masc),
            "ec_ndn_masc": len(ec_ndn_masc),

            "opcao": opcao,
            "entrada": entrada,
            "min": calcular_idade(data_maxima),
            "max": calcular_idade(data_minima),
            'most_common_variavel': most_common_variavel_value,

        }

        return render(request, "pacientes/filtros.html", context)
    else:
        todos_pacientes = Paciente.objects.all()
        qtd1 = todos_pacientes.count()
        qtd2 = Paciente.objects.all().count()
        percent = (qtd1 / qtd2) * 100
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
        "pacientes": pacientes,
        "qtd1": qtd1,
        "percent": percent,
        "opcao": opcao,
        "entrada": entrada,
        'most_common_variavel': most_common_variavel_value,

    }
    return render(request, "pacientes/filtros.html", context)
#comentario