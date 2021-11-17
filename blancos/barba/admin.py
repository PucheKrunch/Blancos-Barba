from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Iva)
admin.site.register(Proveedor)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Compra)
admin.site.register(DetalleCompra)
admin.site.register(Baja)
admin.site.register(DetalleBaja)