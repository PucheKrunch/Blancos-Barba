"""blancos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('addemp/',views.addemp, name='addemp'),
    path('emps/',views.emps, name='emps'),
    path('memp/<str:pk>',views.memp, name='memp'),
    path('addclient/',views.addclient, name='addclient'),
    path('clients/',views.clients, name='clients'),
    path('mclient/<str:pk>',views.mclient, name='mclient'),
    path('addproduct/',views.addproduct, name='addproduct'),
    path('products/',views.products, name='products'),
    path('mproduct/<str:pk>',views.mproduct, name='mproduct'),
    path('iva/',views.iva, name='iva'),
    path('addprov/',views.addprov, name='addprov'),
    path('provs/',views.provs, name='provs'),
    path('mprov/<str:pk>',views.mprov, name='mprov'),
    path('addbaja/',views.addbaja, name='addbaja'),
    path('bajas/',views.bajas, name='bajas'),
    path('addventa/',views.addventa, name='addventa'),
    path('ventas/',views.ventas, name='ventas'),
    path('statusventa/',views.statusventa, name='statusventa'),
    path('addcompra/',views.addcompra, name='addcompra'),
    path('compras/',views.compras, name='compras'),
]