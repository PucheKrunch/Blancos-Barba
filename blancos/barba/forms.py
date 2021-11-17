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