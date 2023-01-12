from django import forms
from django.forms import fields
from prontuario.models import Prontuario


class ProntuarioForm(forms.ModelForm):
    class Meta:
        model = Prontuario
        fields = "__all__"

# class DadosMedicosForm(forms.ModelForm):
#     class Meta:
#         model = DadosMedicos
#         fields = "__all__"