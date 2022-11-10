from rest_framework import serializers
from apps.ventas.models import *

class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields=('__all__')
