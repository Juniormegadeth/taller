from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.clientes.models import *
from apps.clientes.serializers import *

# Clientes

class ClientesView(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

    def get(self, request, *args, **kwargs):
        clientesData = ClientesSerializer(self.get_queryset(), many=True)
        return Response(clientesData.data, status=status.HTTP_200_OK)

class ClientesViewOwner(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

    def get(self, request, *args, **kwargs):
        ClientesData = ClientesSerializer(self.get_queryset(), many=True)
        return Response(ClientesData.data, status=status.HTTP_200_OK)

class ClientesCreate(CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

    def post(self, request, *args, **kwargs):
        createData = ClientesSerializer(data=request.data)
        if createData.is_valid():
            createData.save()
            return Response(createData.data, status=status.HTTP_200_OK)
        return Response(createData.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientesUpdate(UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer


class ClientesDelete(DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer
