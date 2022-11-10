from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.productos.models import *
from apps.productos.serializers import *

# Productos

class ProductosView(ListAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

    def get(self, request, *args, **kwargs):
        productosData = ProductosSerializer(self.get_queryset(), many=True)
        return Response(productosData.data, status=status.HTTP_200_OK)

class ProductosViewOwner(ListAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

    def get(self, request, *args, **kwargs):
        ProductosData = ProductosSerializer(self.get_queryset(), many=True)
        return Response(ProductosData.data, status=status.HTTP_200_OK)

class ProductosCreate(CreateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

    def post(self, request, *args, **kwargs):
        createData = ProductosSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductosUpdate(UpdateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer


class ProductosDelete(DestroyAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

# Tipo Productos

class TipoProductoView(ListAPIView):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

    def get(self, request, *args, **kwargs):
        tipoproductoData = TipoProductoSerializer(self.get_queryset(), many=True)
        return Response(tipoproductoData.data, status=status.HTTP_200_OK)

class TipoProductoViewOwner(ListAPIView):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

    def get(self, request, *args, **kwargs):
        TipoProductoData = TipoProductoSerializer(self.get_queryset(), many=True)
        return Response(TipoProductoData.data, status=status.HTTP_200_OK)

class TipoProductoCreate(CreateAPIView):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

    def post(self, request, *args, **kwargs):
        createData = TipoProductoSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class TipoProductoUpdate(UpdateAPIView):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer


class TipoProductoDelete(DestroyAPIView):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer
    

# Productos Venta

class ProductoVentaView(ListAPIView):
    queryset = ProductoVenta.objects.all()
    serializer_class = ProductoVentaSerializer

    def get(self, request, *args, **kwargs):
        productoventaData = ProductoVentaSerializer(self.get_queryset(), many=True)
        return Response(productoventaData.data, status=status.HTTP_200_OK)

class ProductoVentaViewOwner(ListAPIView):
    queryset = ProductoVenta.objects.all()
    serializer_class = ProductoVentaSerializer

    def get(self, request, *args, **kwargs):
        ProductoVentaData = ProductoVentaSerializer(self.get_queryset(), many=True)
        return Response(ProductoVentaData.data, status=status.HTTP_200_OK)

class ProductoVentaCreate(CreateAPIView):
    queryset = ProductoVenta.objects.all()
    serializer_class = ProductoVentaSerializer

    def post(self, request, *args, **kwargs):
        createData = ProductoVentaSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoVentaUpdate(UpdateAPIView):
    queryset = ProductoVenta.objects.all()
    serializer_class = ProductoVentaSerializer


class ProductoVentaDelete(DestroyAPIView):
    queryset = ProductoVenta.objects.all()
    serializer_class = ProductoVentaSerializer