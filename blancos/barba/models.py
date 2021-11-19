from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=50,null=True)
    apellidos = models.CharField(max_length=50,null=True)
    sueldo = models.FloatField(null=True)
    cargo = models.CharField(max_length=50,null=True)
    direccion = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True,blank=True)
    password = models.CharField(max_length=50,null=True)
    telefono = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos

class Cliente(models.Model):
    nombre = models.CharField(max_length=50,null=True)
    apellidos = models.CharField(max_length=50,null=True)
    correo = models.CharField(max_length=50,null=True)
    telefono = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos

class Iva(models.Model):
    porcentaje = models.FloatField(null=True)
    fecha_aplicacion = models.DateField(null=True,blank=True)
    fecha_termino = models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.porcentaje)

class Producto(models.Model):
    descripcion = models.CharField(max_length=50,null=True)
    precio = models.FloatField(null=True)
    color = models.CharField(max_length=50,null=True)
    talla = models.CharField(max_length=50,null=True)
    existencia = models.IntegerField(null=True)

    def __str__(self):
        return self.descripcion

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50,null=True,blank=True)
    correo = models.CharField(max_length=50,null=True,blank=True)
    telefono = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fechaVenta = models.DateField(null=True,blank=True)
    fechaEntrega = models.DateField(null=True,blank=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL,null=True,blank=True)
    vendedor = models.ForeignKey(Empleado,on_delete=models.SET_NULL,null=True,blank=True)
    repartidor = models.ForeignKey(Empleado,on_delete=models.SET_NULL,null=True,blank=True,related_name='repartidor')
    direccion = models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.cliente.nombre) + ' ' + str(self.cliente.apellidos) + ' ' + str(self.id)

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta,on_delete=models.CASCADE,null=True,blank=True)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,null=True,blank=True)
    cantidad = models.IntegerField(null=True,blank=True)
    precio = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.venta.cliente.nombre) + ' ' + str(self.venta.cliente.apellidos) + ' ' + str(self.venta.id)

class Compra(models.Model):
    fechaCompra = models.DateField(null=True,blank=True)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True,blank=True)
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.proveedor.nombre

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra,on_delete=models.CASCADE,null=True,blank=True)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,null=True,blank=True)
    cantidad = models.IntegerField(null=True,blank=True)
    precio = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.compra.proveedor.nombre

class Baja(models.Model):
    fechaBaja = models.DateField(null=True,blank=True)
    compra = models.ForeignKey(Compra,on_delete=models.CASCADE,null=True,blank=True)
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.fechaBaja)

class DetalleBaja(models.Model):
    baja = models.ForeignKey(Baja,on_delete=models.CASCADE,null=True,blank=True)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,null=True,blank=True)
    cantidad = models.IntegerField(null=True,blank=True)
    motivo = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return str(self.baja.fechaBaja)