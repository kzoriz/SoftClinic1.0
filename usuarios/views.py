from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from usuarios.forms import UserCreationForm
from django.contrib import messages
from .models import Funcionario, Docente, Discente
from django.contrib.auth.models import User

def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('login')
    return render(request, 'usuarios/signup.html', {'form': form})


def cadastro_funcionario(request):
    template_name = 'usuarios/funcionario_cadastro.html'

    titulo = 'Cadastrar Funcionario'
    context = {
        'titulo': titulo,
    }
    if request.method == 'POST':
        matricula = request.POST['matricula']
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']

        if not nome or not matricula or not telefone or not email or not senha1 or not senha2:
            messages.error(request, 'Não é permitido campos vazios')
            return render(request, template_name)

        if senha1 != senha2:
            messages.error(request, 'Senhas não conferem.')
            return render(request, template_name)

        u = User.objects.create_user(username=nome, email=None, password=senha1)
        u.save()
        c = Funcionario(usuario=u, matricula=matricula, nome=nome, telefone=telefone, email=email)
        c.save()
        messages.success(request, 'Funcionario Cadastrado!')
        return redirect('inicio')
    return render(request, template_name, context)


def cadastro_docente(request):
    template_name = 'usuarios/docente_cadastro.html'
    titulo = 'Cadastrar Docente'
    context = {
        'titulo': titulo,
    }
    if request.method == 'POST':
        matricula = request.POST['matricula']
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']

        if not nome or not matricula or not telefone or not email or not senha1 or not senha2:
            messages.error(request, 'Não é permitido campos vazios')
            return render(request, template_name)

        if senha1 != senha2:
            messages.error(request, 'Senhas não conferem.')
            return render(request, template_name)

        u = User.objects.create_user(username=nome, email=None, password=senha1)
        u.save()
        c = Docente(nome=nome, email=email, matricula=matricula, telefone=telefone, usuario=u)
        c.save()
        messages.success(request, 'Docente Cadastrado!')
        return redirect('inicio')
    return render(request, template_name, context)


def cadastro_discente(request):
    template_name = 'usuarios/discente_cadastro.html'
    titulo = 'Cadastrar Discente'
    context = {
        'titulo': titulo,
    }
    if request.method == 'POST':
        matricula = request.POST['matricula']
        periodo = request.POST['periodo']
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']

        if not nome or not matricula or not telefone or not email or not senha1 or not senha2:
            messages.error(request, 'Não é permitido campos vazios')
            return render(request, template_name)

        if senha1 != senha2:
            messages.error(request, 'Senhas não conferem.')
            return render(request, template_name)

        u = User.objects.create_user(username=nome, email=None, password=senha1)
        u.save()
        c = Discente(nome=nome, email=email, matricula=matricula, periodo=periodo, telefone=telefone, usuario=u)
        c.save()
        messages.success(request, 'Discente Cadastrado!')
        return redirect('inicio')
    return render(request, template_name, context)

