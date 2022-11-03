from django.contrib import admin

from pacientes.models import Paciente, PacienteInfantil, Teste, Teste2

# Register your models here.
admin.site.register(Paciente)
admin.site.register(PacienteInfantil)\

@admin.register(Teste)
class TesteAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Teste2)
class Teste2Admin(admin.ModelAdmin):
    exclude = ()

