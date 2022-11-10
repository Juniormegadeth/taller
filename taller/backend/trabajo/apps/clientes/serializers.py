from rest_framework import serializers
from apps.clientes.models import *

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields=('__all__')
