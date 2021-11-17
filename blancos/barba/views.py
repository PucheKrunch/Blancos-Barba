from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

#login del empleado
def login(request):
    return render(request, 'login.html')

#Formulario para agregar empleados
def addemp(request):
    if request.method == 'POST':
        form = AddEmpleadoForm(request.POST)
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        sueldo = request.POST['sueldo']
        password = request.POST['password']
        try:
            cargo = request.POST['cargo']
        except:
            context = {
                'nombre': nombre,
                'apellidos': apellidos,
                'direccion': direccion,
                'telefono': telefono,
                'sueldo': sueldo,
            }
            messages.error(request, 'Selecciona un cargo por favor')
            return render(request, 'addemp.html', context)
        cargo = request.POST['cargo']
        context = {
            'nombre': nombre,
            'apellidos': apellidos,
            'direccion': direccion,
            'cargo': cargo,
            'telefono': telefono,
            'sueldo': sueldo,
            'password': password,
        }

        if form.is_valid():
            form.save()
            empleado = list(Empleado.objects.all())[-1]
            empleado.status = "Activo"
            empleado.save()
            return redirect('emps')
        else:
            messages.error(request, 'Completa el formulario por favor')
            return render(request, 'addemp.html', context)
    return render(request, 'addemp.html')

#Lista de empleados
def emps(request):
    if request.method == 'POST':
        empleados = Empleado.objects.filter(apellidos__contains=request.POST['searched'])
        flag = 1 if len(empleados) > 0 else 2
    else:
        empleados = Empleado.objects.all()
        flag = 0
    context = {
        'empleados': empleados,
        'flag': flag,
    }
    return render(request, 'emps.html', context)

#Modificar empleado
def memp(request,pk):
    if request.method == 'POST':
        form = ModifyEmpleadoForm(request.POST)
        try:
            cargo = request.POST['cargo']
        except:
            empleado = Empleado.objects.get(pk=pk)
            context = {
                'empleado': empleado,
            }
            messages.error(request, 'Selecciona un cargo por favor')
            return render(request, 'memp.html', context)
        cargo = request.POST['cargo']
        status = request.POST['status']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        sueldo = request.POST['sueldo']
        context = {
            'cargo': cargo,
            'status': status,
            'direccion': direccion,
            'telefono': telefono,
            'sueldo': sueldo,
        }
        if form.is_valid():
            empleado = Empleado.objects.get(pk=pk)
            empleado.cargo = cargo
            empleado.status = status
            empleado.direccion = direccion
            empleado.telefono = telefono
            empleado.sueldo = sueldo
            empleado.save()
            return redirect('emps')
        else:
            empleado = Empleado.objects.get(pk=pk)
            context = {
                'empleado': empleado,
            }
            messages.error(request, 'No dejes campos en blanco por favor')
            return render(request, 'memp.html', context)
    else:
        empleado = Empleado.objects.get(pk=pk)
        context = {
            'empleado': empleado,
        }
        return render(request, 'memp.html', context)

#Formulario para agregar clientes
def addclient(request):
    return render(request, 'addclient.html')

#Lista de clientes
def clients(request):
    return render(request, 'clients.html')

#Modificar cliente
def mclient(request,pk):
    return render(request, 'mclient.html')

#Formulario para agregar productos
def addproduct(request):
    return render(request, 'addproduct.html')

#Lista de productos
def products(request):
    return render(request, 'products.html')

#Modificar existencia de productos
def mproduct(request,pk):
    return render(request, 'mproduct.html')

#Modificar iva
def iva(request):
    return render(request, 'iva.html')

#Formulario para agregar proveedores
def addprov(request):
    return render(request, 'addprov.html')

#Lista de proveedores
def provs(request):
    return render(request, 'provs.html')

#Modificar proveedor
def mprov(request,pk):
    return render(request, 'mprov.html')

#Formulario para agregar bajas
def addbaja(request):
    return render(request, 'addbaja.html')

#Lista de bajas
def bajas(request):
    return render(request, 'bajas.html')

#Formulario para agregar ventas
def addventa(request):
    return render(request, 'addventa.html')

#Lista de ventas
def ventas(request):
    return render(request, 'ventas.html')

#Modificar status de venta
def statusventa(request):
    return render(request, 'statusventa.html')

#Formulario para agregar compras
def addcompra(request):
    return render(request, 'addcompra.html')

#Lista de compras
def compras(request):
    return render(request, 'compras.html')