from django.contrib import admin
from apps.productos.models import *
# Register your models here.

admin.site.register(Productos)
admin.site.register(ProductoVenta)
admin.site.register(TipoProducto)