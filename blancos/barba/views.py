from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

#login del empleado
def login(request):
    return render(request, 'login.html')

#Formulario para agregar empleados
def addemp(request):
    return render(request, 'addemp.html')

#Lista de empleados
def emps(request):
    return render(request, 'emps.html')

#Modificar empleado
def memp(request,pk):
    return render(request, 'memp.html')

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