from django.contrib import admin
from usuarios.models import Funcionario, Docente, Discente


admin.site.register(Funcionario)
admin.site.register(Docente)
admin.site.register(Discente)
