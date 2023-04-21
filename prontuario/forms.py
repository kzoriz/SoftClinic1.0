from django import forms
from django.forms import fields
from prontuario.models import *


# class ProntuarioForm(forms.ModelForm):
#     class Meta:
#         model = Prontuario
#         fields = "__all__"
#

class DenteForm(forms.ModelForm):
    class Meta:
        model = Dente
        fields = ['distal', ]
