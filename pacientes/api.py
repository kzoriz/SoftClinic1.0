import json
from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from ninja.orm import create_schema

from .models import Paciente

router = Router()

PacienteSchema = create_schema(Paciente)


@router.get('/pacientes', response=List[PacienteSchema])
def list_customers(request):
    qs = Paciente.objects.all()
    return qs


@router.get('/pacientes/{id}', response=PacienteSchema)
def get_customer(request, id: int):
    paciente = get_object_or_404(Paciente, id=id)
    return paciente


@router.post('/pacientes', response={201: PacienteSchema})
def create_customer(request, payload: PacienteSchema):
    paciente = Paciente.objects.create(**payload.dict())
    # Pegando valores adicionais passados no corpo da requisição.
    data = json.loads(request.body)
    a = data.get('a')
    b = data.get('b')
    print(a + b)
    return 201, paciente


@router.put('/pacientes/{id}', response=PacienteSchema)
def update_customer(request, id: int, payload: PacienteSchema):
    paciente = get_object_or_404(Paciente, id=id)

    for attr, value in payload.dict().items():
        setattr(paciente, attr, value)

    paciente.save()
    return paciente


@router.delete('/pacientes/{id}', response={204: None})
def delete_customer(request, id: int):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return 204, None


