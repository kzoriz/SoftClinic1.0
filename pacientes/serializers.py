from pacientes.models import Teste2, Teste
from rest_framework import serializers


class Teste2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Teste2
        fields = '__all__'


class TesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teste
        fields = '__all__'