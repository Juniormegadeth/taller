from django.db import models
from apps.clientes.models import *

# Create your models here.

class Ventas(models.Model):
    fecha_entrada = models.DateField()
    subtotal = models.FloatField()
    impuestos = models.FloatField()
    descuentos = models.FloatField()
    total = models.FloatField()
    venta = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.venta
