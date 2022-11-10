from django.db import models
from apps.clientes.models import *

# Create your models here.

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    precio = models.FloatField()
    stockMin = models.FloatField()
    cantidad = models.FloatField()
    tipoproducto = models.ForeignKey(TipoProducto, null=True, blank=True, on_delete=models.CASCADE)
    cliente = models.ManyToManyField(Cliente, through='ProductoVenta')
    
    def __str__(self):
        return self.nombre

class ProductoVenta(models.Model):
    producto = models.ForeignKey(Productos, null=True, blank=True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=255)
    precio = models.CharField(max_length=255)
    total = models.CharField(max_length=255)

    def __str__(self):
        return self.cantidad



