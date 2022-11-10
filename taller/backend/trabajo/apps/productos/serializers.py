from rest_framework import serializers
from apps.productos.models import *

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields=('__all__')

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields=('__all__')

class ProductoVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoVenta
        fields=('__all__')