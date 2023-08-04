from django.db import models

class Cliente(models.Model):
    documento = models.CharField(max_length=20, choices=[('cédula', 'Cédula'), ('ruc', 'RUC'), ('pasaporte', 'Pasaporte')])  # Adjust the max_length for the documento field
    documento_detalle = models.IntegerField(default=1000000000, verbose_name='Número de cédula')
    apellido = models.CharField(max_length=50)
    dirección = models.CharField(max_length=100)
    teléfono = models.IntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Producto(models.Model):
    código = models.IntegerField(primary_key=True)
    descripción = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    número = models.IntegerField(primary_key=True)
    fecha = models.DateField(auto_now=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    observaciones = models.CharField(max_length=50, verbose_name='Observaciones de la venta')
    iva = models.FloatField(choices=[(0.12, '12%')])
    descuento = models.FloatField(choices=[(0.1, '10%'), (0.2, '20%'), (0.3, '30%')])

    @property
    def total_calculado(self):
        subtotal = self.producto.precio * self.cantidad
        total = subtotal + (subtotal * self.iva) - (subtotal * self.descuento)
        return total

    def __str__(self):
        return f"{self.cliente} - {self.producto}, ha adquirido una {self.producto.nombre} por el costo total de: {self.total_calculado}"
