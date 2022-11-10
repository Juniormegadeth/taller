from django.contrib import admin
from apps.ventas.models import *
# Register your models here.

class VentasAdmin(admin.ModelAdmin):
    list_display = ('fecha_entrada', 'subtotal', 'impuestos','descuentos','total','venta','cliente')
    ordering = ('fecha_entrada', 'subtotal', 'impuestos','descuentos','total','venta','cliente')
    search_fields = ('fecha_entrada', 'subtotal', 'impuestos','descuentos','total','venta','cliente')
    list_filter = ('fecha_entrada','subtotal')


admin.site.register(Ventas,VentasAdmin)