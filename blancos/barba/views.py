from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *
from datetime import date

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
        if int(sueldo) <= 0:
            context = {
                'nombre': nombre,
                'apellidos': apellidos,
                'direccion': direccion,
                'telefono': telefono,
            }
            messages.error(request, 'El sueldo no puede ser negativo o 0')
            return render(request, 'addemp.html', context)
            messages.error(request, 'El sueldo no puede ser negativo o 0')
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
        if int(sueldo) <= 0:
            messages.error(request, 'El sueldo no puede ser negativo o 0')
            return redirect('memp',pk)
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
    if request.method == 'POST':
        form = AddClienteForm(request.POST)
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        if form.is_valid():
            form.save()
            return redirect('clients')
        else:
            context = {
                'nombre': nombre,
                'apellidos': apellidos,
                'correo': correo,
                'telefono': telefono,
            }
            messages.error(request, 'Completa el formulario por favor')
            return render(request, 'addclient.html', context)
    return render(request, 'addclient.html')

#Lista de clientes
def clients(request):
    if request.method == 'POST':
        clientes = Cliente.objects.filter(apellidos__contains=request.POST['searched'])
        flag = 1 if len(clientes) > 0 else 2
    else:
        clientes = Cliente.objects.all()
        flag = 0
    context = {
        'clientes': clientes,
        'flag': flag,
    }
    return render(request, 'clients.html', context)

#Modificar cliente
def mclient(request,pk):
    if request.method == 'POST':
        form = ModifyClienteForm(request.POST)
        if form.is_valid():
            cliente = Cliente.objects.get(pk=pk)
            cliente.correo = request.POST['correo']
            cliente.telefono = request.POST['telefono']
            cliente.save()
            return redirect('clients')
        else:
            cliente = Cliente.objects.get(pk=pk)
            context = {
                'cliente': cliente,
            }
            messages.error(request, 'No dejes campos en blanco por favor')
            return render(request,'mclient.html',context)
    else:
        cliente = Cliente.objects.get(pk=pk)
        context = {
            'cliente': cliente,
        }
        return render(request, 'mclient.html', context)

#Formulario para agregar productos
def addproduct(request):
    if request.method == 'POST':
        form = AddProductoForm(request.POST)
        descripcion = request.POST['descripcion']
        color = request.POST['color']
        precio = request.POST['precio']
        existencia = request.POST['existencia']
        context = {
                'descripcion': descripcion,
                'color': color,
                'precio': precio,
                'existencia': existencia,
            }
        if int(precio) <= 0 or int(existencia) <= 0:
            messages.error(request, 'El precio y la existencia no pueden ser negativos o 0')
            return render(request, 'addproduct.html',context)
        try:
            talla = request.POST['talla']
        except:
            messages.error(request, 'Selecciona una talla por favor')
            return render(request, 'addproduct.html', context)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            messages.error(request, 'Completa el formulario por favor')
            return render(request, 'addproduct.html', context)
    else:
        return render(request, 'addproduct.html')

#Lista de productos
def products(request):
    if request.method == 'POST':
        productos = Producto.objects.filter(descripcion__contains=request.POST['searched'])
        flag = 1 if len(productos) > 0 else 2
    else:
        productos = Producto.objects.all()
        flag = 0
    context = {
        'productos': productos,
        'flag': flag,
    }
    return render(request, 'products.html', context)

#Modificar existencia de productos
def mproduct(request,pk):
    producto = Producto.objects.get(pk=pk)
    context = {
        'producto': producto,
    }
    if request.method == 'POST':
        form = ModifyProductoForm(request.POST)
        existencia = request.POST['existencia']
        if int(existencia) <= 0:
            messages.error(request, 'La existencia no puede ser negativa o 0')
            return redirect('mproduct',pk)
        if form.is_valid():
            producto = Producto.objects.get(pk=pk)
            producto.existencia = existencia
            producto.save()
            return redirect('products')
        else:
            messages.error(request, 'Completa el formulario por favor')
            return redirect('mproduct',pk)
    return render(request, 'mproduct.html', context)

#Modificar iva
def iva(request):
    ivas = Iva.objects.all()
    actual = list(Iva.objects.all())[-1]
    context = {
        'ivas': ivas,
        'actual': actual,
    }
    if request.method == 'POST':
        try:
            porcentaje = request.POST['porcentaje']
            Iva.objects.create(porcentaje=porcentaje, fecha_aplicacion=date.today())
        except:
            messages.error(request, 'Ingrese un porcentaje por favor')
            return render(request, 'iva.html', context)
        actual.fecha_termino = date.today()
        actual.save()
        return redirect('iva')
    return render(request, 'iva.html',context)

#Formulario para agregar proveedores
def addprov(request):
    if request.method == 'POST':
        form = AddProveedorForm(request.POST)
        correo = request.POST['correo']
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        if form.is_valid():
            form.save()
            return redirect('provs')
        else:
            context = {
                'nombre': nombre,
                'correo': correo,
                'telefono': telefono,
            }
            messages.error(request, 'Completa el formulario por favor')
            return render(request, 'addprov.html', context)
    return render(request, 'addprov.html')

#Lista de proveedores
def provs(request):
    if request.method == 'POST':
        proveedores = Proveedor.objects.filter(nombre__contains=request.POST['searched'])
        flag = 1 if len(proveedores) > 0 else 2
    else:
        proveedores = Proveedor.objects.all()
        flag = 0
    context = {
        'proveedores': proveedores,
        'flag': flag,
    }
    return render(request, 'provs.html', context)

#Modificar proveedor
def mprov(request,pk):
    if request.method == 'POST':
        form = ModifyProveedorForm(request.POST)
        if form.is_valid():
            proveedor = Proveedor.objects.get(pk=pk)
            proveedor.correo = request.POST['correo']
            proveedor.telefono = request.POST['telefono']
            proveedor.save()
            return redirect('provs')
        else:
            messages.error(request, 'Completa el formulario por favor')
            return redirect('mprov',pk)
    else:
        proveedor = Proveedor.objects.get(pk=pk)
        context = {
            'proveedor': proveedor,
        }
        return render(request, 'mprov.html', context)

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