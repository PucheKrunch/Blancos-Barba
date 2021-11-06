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

#Modificar cliente
def memp(request,pk):
    return render(request, 'memp.html')