from django.contrib.auth import forms
from usuarios.models import User, Funcionario, Discente
from django import forms as mforms
from django import forms as xforms


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User


class FuncionarioForm(mforms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'


class DiscenteForm(xforms.ModelForm):
    class Meta:
        model = Discente
        fields = "__all__"

