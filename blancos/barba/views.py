from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *
from datetime import date, timedelta

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
        empleados = Empleado.objects.filter(pk=request.POST['searched']) if request.POST['searched'].isnumeric() else Empleado.objects.filter(apellidos__contains=request.POST['searched'])
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
        clientes = Cliente.objects.filter(pk=request.POST['searched']) if request.POST['searched'].isnumeric() else Cliente.objects.filter(apellidos__contains=request.POST['searched'])
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
        productos = Producto.objects.filter(pk=request.POST['searched']) if request.POST['searched'].isnumeric() else Producto.objects.filter(descripcion__contains=request.POST['searched'])
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
        proveedores = Proveedor.objects.filter(pk=request.POST['searched']) if request.POST['searched'].isnumeric() else Proveedor.objects.filter(nombre__contains=request.POST['searched'])
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
    empleados = Empleado.objects.filter(cargo__in=['Administrador','Almacenista'])
    detalles = DetalleBaja.objects.filter(baja=list(Baja.objects.all())[-1])
    context = {
        'empleados': empleados,
        'detalles': detalles,
        'flag': len(detalles),
    }
    if request.method == 'POST':
        baja = list(Baja.objects.all())[-1]
        try:
            baja.empleado = Empleado.objects.get(pk=request.POST['empleado'])
        except:
            messages.error(request, 'Completa el formulario correctamente por favor')
            return render(request, 'addbaja.html', context)
        compra = Compra.objects.filter(pk=int(request.POST['compra']))
        if len(compra) == 0:
            messages.error(request, 'No existe esa compra')
            return render(request, 'addbaja.html', context)
        baja.compra = compra[0]
        baja.fechaBaja = date.today()
        baja.save()
        Baja.objects.create()
        return redirect('bajainfo',baja.pk)
    return render(request, 'addbaja.html', context)

#Lista de bajas
def bajas(request):
    if request.method == 'POST':
        if request.POST['searched'] == '':
            bajas = Baja.objects.all().exclude(fechaBaja=None)
            flag = 0
        else:
            bajas = Baja.objects.filter(pk=request.POST['searched']).exclude(fechaBaja=None)
            flag = 1 if len(bajas) > 0 else 2
    else:
        bajas = Baja.objects.all().exclude(fechaBaja=None)
        flag = 0
    context = {
        'bajas': bajas,
        'flag': flag,
    }
    return render(request, 'bajas.html', context)

#Agregar producto a baja
def addpb(request):
    baja = list(Baja.objects.all())[-1]
    if request.method == 'POST':
        if request.POST['producto'] != '' and request.POST['cantidad'] != '' and request.POST['motivo'] != '':
            try:
                producto = Producto.objects.get(pk=request.POST['producto'])
            except:
                messages.error(request, 'El producto no existe')
                return redirect('addbaja')
            else:
                if int(request.POST['cantidad']) <= 0:
                    messages.error(request, 'La cantidad no puede ser negativa o 0')
                    return redirect('addbaja')
                else:
                    if len(DetalleBaja.objects.filter(producto=producto, baja=baja)) > 0:
                        detalle = DetalleBaja.objects.get(producto=producto, baja=baja)
                        detalle.cantidad += int(request.POST['cantidad'])
                        detalle.motivo = request.POST['motivo']
                        detalle.save()
                        producto.existencia -= int(request.POST['cantidad'])
                        producto.save()
                    else:
                        DetalleBaja.objects.create(producto=producto, cantidad=int(request.POST['cantidad']), baja=baja, motivo=request.POST['motivo'])
                        producto.existencia -= int(request.POST['cantidad'])
                        producto.save()
                    return redirect('addbaja')
            return redirect('addbaja')
        else:
            messages.error(request, 'Completa el formulario de productos por favor')
            return redirect('addbaja')

#Información de la baja
def bajainfo(request,pk):
    baja = Baja.objects.get(pk=pk)
    detalles = DetalleBaja.objects.filter(baja=baja)
    context = {
        'baja': baja,
        'detalles': detalles,
    }
    return render(request, 'bajainfo.html', context)

#Eliminar producto de baja
def delpb(request,pk):
    producto = Producto.objects.get(pk=pk)
    detalle = DetalleBaja.objects.get(producto=producto, baja=list(Baja.objects.all())[-1])
    producto.existencia += detalle.cantidad
    producto.save()
    detalle.delete()
    return redirect('addbaja')

#Borrar todos los productos de una baja
def delallpb(request):
    detalles = DetalleBaja.objects.filter(baja=list(Baja.objects.all())[-1])
    for detalle in detalles:
        producto = Producto.objects.get(pk=detalle.producto.pk)
        producto.existencia += detalle.cantidad
        producto.save()
    detalles.delete()
    return redirect('addbaja')

#Formulario para agregar ventas
def addventa(request):
    repartidores = Empleado.objects.filter(cargo='Repartidor')
    vendedores = Empleado.objects.filter(cargo='Vendedor')
    detalles = DetalleVenta.objects.filter(venta=list(Venta.objects.all())[-1])
    productos = []
    subtotal = 0
    for detalle in detalles:
        p = Producto.objects.get(pk=detalle.producto.pk)
        subtotal += p.precio * detalle.cantidad
        productos.append({
            'producto': p,
            'cantidad': detalle.cantidad,
            'pc': p.precio * detalle.cantidad,
        })
    context = {
        'productos': productos,
        'subtotal': subtotal,
        'flag': len(productos),
        'repartidores': repartidores,
        'vendedores': vendedores,
    }
    if request.method == 'POST':
        try:
            venta = list(Venta.objects.all())[-1]
            venta.vendedor = Empleado.objects.get(pk=request.POST['vendedor'])
            venta.repartidor = Empleado.objects.get(pk=request.POST['repartidor'])
        except:
            messages.error(request, 'Completa el formulario correctamente por favor')
            return render(request, 'addventa.html', context)
        else:
            if len(Cliente.objects.filter(pk=request.POST['cliente'])) == 0:
                messages.error(request, 'El cliente no existe')
                return render(request, 'addventa.html', context)
            else:
                venta.fechaVenta = date.today()
                venta.fechaEntrega = date.today() + timedelta(days=7)
                venta.cliente = Cliente.objects.get(pk=request.POST['cliente'])
                if request.POST['direccion'] == '':
                    messages.error(request, 'Ingrese una dirección por favor')
                    return render(request, 'addventa.html', context)
                venta.direccion = request.POST['direccion']
                venta.status = 'Preparando entrega'
                venta.save()
                Venta.objects.create()
                return redirect('statusventa',venta.pk)
    return render(request, 'addventa.html', context)

#Añadir producto a venta
def addpv(request):
    venta = list(Venta.objects.all())[-1]
    if request.method == 'POST':
        if request.POST['producto'] != '' and request.POST['cantidad'] != '':
            try:
                producto = Producto.objects.get(pk=request.POST['producto'])
            except:
                messages.error(request, 'El producto no existe')
                return redirect('addventa')
            else:
                if int(request.POST['cantidad']) <= 0:
                    messages.error(request, 'La cantidad no puede ser negativa o 0')
                    return redirect('addventa')
                elif producto.existencia < int(request.POST['cantidad']):
                    messages.error(request, 'No hay suficiente existencia')
                    return redirect('addventa')
                else:
                    if len(DetalleVenta.objects.filter(venta=venta).filter(producto=request.POST['producto'])) > 0:
                        detalle = DetalleVenta.objects.get(venta=venta, producto=request.POST['producto'])
                        detalle.cantidad += int(request.POST['cantidad'])
                        detalle.save()
                        producto.existencia -= int(request.POST['cantidad'])
                        producto.save()
                    else:
                        producto.existencia -= int(request.POST['cantidad'])
                        producto.save()
                        DetalleVenta.objects.create(venta=venta, producto=producto, cantidad=request.POST['cantidad'])
                    return redirect('addventa')
            return redirect('addventa')
        else:
            messages.error(request, 'Completa el formulario de productos por favor')
            return redirect('addventa')

#Eliminar producto de nota de venta
def delpv(request,pk):
    producto = Producto.objects.get(pk=pk)
    detalle = DetalleVenta.objects.get(producto=producto, venta=list(Venta.objects.all())[-1])
    producto.existencia += detalle.cantidad
    producto.save()
    detalle.delete()
    return redirect('addventa')

#Borrar todos los productos de una venta
def delallpv(request):
    detalles = DetalleVenta.objects.filter(venta=list(Venta.objects.all())[-1])
    for detalle in detalles:
        producto = Producto.objects.get(pk=detalle.producto.pk)
        producto.existencia += detalle.cantidad
        producto.save()
    detalles.delete()
    return redirect('addventa')

#Lista de ventas
def ventas(request):
    if request.method == 'POST':
        ventas = Venta.objects.filter(pk=request.POST['searched']).exclude(status=None) if request.POST['searched'].isnumeric() else Venta.objects.filter(cliente__apellidos__icontains=request.POST['searched'])
        flag = 1 if len(ventas) > 0 else 2
    else:
        ventas = Venta.objects.all().exclude(status=None)
        flag = 0
    context = {
        'ventas': ventas,
        'flag': flag,
    }
    return render(request, 'ventas.html', context)

#Modificar status de venta
def statusventa(request,pk):
    if request.method == 'POST':
        form = ModifyVentaForm(request.POST)
        if form.is_valid():
            venta = Venta.objects.get(pk=pk)
            venta.status = request.POST['status']
            venta.save()
            if venta.status == 'Cancelada':
                detalles = DetalleVenta.objects.filter(venta=venta)
                for detalle in detalles:
                    producto = Producto.objects.get(pk=detalle.producto.pk)
                    producto.existencia += detalle.cantidad
                    producto.save()
            return redirect('statusventa',pk)
        else:
            messages.error(request, 'Selecciona un status a cambiar')
            return redirect('statusventa',pk)
    venta = Venta.objects.get(pk=pk)
    detalles = DetalleVenta.objects.filter(venta=venta)
    subtotal = 0
    productos = []
    for detalle in detalles:
        p = Producto.objects.get(pk=detalle.producto.pk)
        subtotal += p.precio * detalle.cantidad
        productos.append({
            'producto': p,
            'cantidad': detalle.cantidad,
            'pc': p.precio * detalle.cantidad,
        })
    iva = list(Iva.objects.all())[-1]
    total = subtotal * (1 + iva.porcentaje/100)
    context = {
        'venta': venta,
        'subtotal': subtotal,
        'iva': iva,
        'total': total,
        'productos': productos,
    }
    return render(request, 'statusventa.html', context)

#Formulario para agregar compras
def addcompra(request):
    empleados = Empleado.objects.filter(cargo__in=['Administrador','Almacenista'])
    proveedores = Proveedor.objects.all()
    detalles = DetalleCompra.objects.filter(compra=list(Compra.objects.all())[-1])
    productos = []
    subtotal = 0
    for detalle in detalles:
        p = Producto.objects.get(pk=detalle.producto.pk)
        subtotal += detalle.precio * detalle.cantidad
        productos.append({
            'producto': p,
            'cantidad': detalle.cantidad,
            'precio': detalle.precio,
            'pc': detalle.precio * detalle.cantidad,
        })
    context = {
        'empleados': empleados,
        'proveedores': proveedores,
        'productos': productos,
        'subtotal': subtotal,
        'flag': len(productos),
    }
    if request.method == 'POST':
        try:
            compra = list(Compra.objects.all())[-1]
            compra.proveedor = Proveedor.objects.get(pk=request.POST['proveedor'])
            compra.empleado = Empleado.objects.get(pk=request.POST['empleado'])
        except:
            messages.error(request, 'Completa el formulario correctamente por favor')
            return render(request, 'addcompra.html', context)
        else:
            compra.fechaCompra = date.today()
            compra.save()
            Compra.objects.create()
            return redirect('comprainfo',compra.pk)
    return render(request, 'addcompra.html', context)

#Añadir productos a compra
def addpc(request):
    compra = list(Compra.objects.all())[-1]
    if request.method == 'POST':
        if request.POST['producto'] != '' and request.POST['cantidad'] != '' and request.POST['precio'] != '':
            try:
                producto = Producto.objects.get(pk=request.POST['producto'])
            except:
                messages.error(request, 'El producto no existe')
                return redirect('addcompra')
            else:
                if int(request.POST['cantidad']) <= 0:
                    messages.error(request, 'La cantidad no puede ser negativa o 0')
                    return redirect('addcompra')
                elif producto.precio <= int(request.POST['precio']):
                    messages.error(request, 'No puedes comprar productos más caros que el precio de venta')
                    return redirect('addcompra')
                else:
                    if len(DetalleCompra.objects.filter(compra=compra,producto=producto)) > 0:
                        detalle = DetalleCompra.objects.get(compra=compra,producto=producto)
                        detalle.cantidad += int(request.POST['cantidad'])
                        detalle.precio = int(request.POST['precio'])
                        detalle.save()
                        producto.existencia += int(request.POST['cantidad'])
                        producto.save()
                    else:
                        DetalleCompra.objects.create(compra=compra,producto=producto,cantidad=int(request.POST['cantidad']),precio=int(request.POST['precio']))
                        producto.existencia += int(request.POST['cantidad'])
                        producto.save()
                    return redirect('addcompra')
            return redirect('addcompra')
        else:
            messages.error(request, 'Completa el formulario de productos por favor')
            return redirect('addcompra')

#Eliminar producto de compra
def delpc(request,pk):
    producto = Producto.objects.get(pk=pk)
    detalle = DetalleCompra.objects.get(compra=list(Compra.objects.all())[-1],producto=producto)
    producto.existencia -= detalle.cantidad
    producto.save()
    detalle.delete()
    return redirect('addcompra')

#Borrar todos los productos de una compra
def delallpc(request):
    detalles = DetalleCompra.objects.filter(compra=list(Compra.objects.all())[-1])
    for detalle in detalles:
        producto = Producto.objects.get(pk=detalle.producto.pk)
        producto.existencia -= detalle.cantidad
        producto.save()
    detalles.delete()
    return redirect('addcompra')

#Lista de compras
def compras(request):
    if request.method == 'POST':
        compras = Compra.objects.filter(pk=request.POST['searched']).exclude(proveedor=None) if request.POST['searched'].isnumeric() else Compra.objects.filter(proveedor__nombre__icontains=request.POST['searched'])
        flag = 1 if len(compras) > 0 else 2
    else:
        compras = Compra.objects.all().exclude(proveedor=None)
        flag = 0
    context = {
        'compras': compras,
        'flag': flag,
    }
    return render(request, 'compras.html', context)

#Información de compra
def comprainfo(request,pk):
    compra = Compra.objects.get(pk=pk)
    detalles = DetalleCompra.objects.filter(compra=compra)
    productos = []
    subtotal = 0
    for detalle in detalles:
        p = Producto.objects.get(pk=detalle.producto.pk)
        subtotal += detalle.precio * detalle.cantidad
        productos.append({
            'producto': p,
            'cantidad': detalle.cantidad,
            'precio': detalle.precio,
            'pc': detalle.precio * detalle.cantidad,
        })
    iva = list(Iva.objects.all())[-1]
    total = subtotal * (1 + iva.porcentaje/100)
    context = {
        'compra': compra,
        'productos': productos,
        'subtotal': subtotal,
        'iva': iva,
        'total': total,
    }
    return render(request, 'comprainfo.html', context)