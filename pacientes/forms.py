from django import forms
from django.forms import fields
from pacientes.models import Paciente, PacienteInfantil


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        exclude = ('num_prontuario',)

class PacienteInfantilForm(forms.ModelForm):
    class Meta:
        model = PacienteInfantil
        fields = "__all__"

