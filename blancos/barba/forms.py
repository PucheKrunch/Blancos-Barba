from django.forms import ModelForm
from .models import *

class AddEmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellidos', 'telefono', 'direccion', 'sueldo', 'cargo', 'password']

class ModifyEmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['telefono', 'direccion', 'sueldo', 'cargo', 'status']

class AddClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'telefono', 'correo']

class ModifyClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['telefono', 'correo']

class AddProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['precio', 'descripcion', 'talla', 'color', 'existencia']

class ModifyProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['existencia']

class AddProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'telefono', 'correo']

class ModifyProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['telefono', 'correo']