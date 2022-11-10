from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=20)
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre
