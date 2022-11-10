from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.ventas.models import *
from apps.ventas.serializers import *

# Ventas

class VentasView(ListAPIView):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer

    def get(self, request, *args, **kwargs):
        ventasData = VentasSerializer(self.get_queryset(), many=True)
        return Response(ventasData.data, status=status.HTTP_200_OK)

class VentasViewOwner(ListAPIView):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer

    def get(self, request, *args, **kwargs):
        VentasData = VentasSerializer(self.get_queryset(), many=True)
        return Response(VentasData.data, status=status.HTTP_200_OK)

class VentasCreate(CreateAPIView):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer

    def post(self, request, *args, **kwargs):
        createData = VentasSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class VentasUpdate(UpdateAPIView):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer

class VentasDelete(DestroyAPIView):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer
