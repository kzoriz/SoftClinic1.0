from django import forms

from distribuicao.models import Disciplina
from pacientes.models import Paciente
from usuarios.models import Discente, Docente
'''
queryset_pacientes = Paciente.objects.all()
queryset_discente = Discente.objects.all()
queryset_docente = Docente.objects.all()
queryset_disciplina = Disciplina.objects.all()
queryset_d = Disciplina.objects.all()
class DistribuicaoForm(forms.Form):
    paciente = forms.ModelChoiceField(queryset_pacientes)
    discente = forms.ModelChoiceField(queryset_discente)
    docente = forms.ModelChoiceField(queryset_docente)
    disciplina = forms.ModelChoiceField(queryset_disciplina)
'''
class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = "__all__"
