Sistema de Ventas de Ropa
Instalar el paquete virtualenv

``` bash 
pip install virtualenv
```

Crear el entorno virtual

``` bash
python -m venv env
```
Activar el entorno virtual

En Windows

``` bash
cd env/Scripts
activate
```
En Linux o Mac

``` bash
source env/bin/activate
```
Instalar Django

``` bash
django-admin startproject tiendavirtual .
```
Crear una aplicación
``` bash
python manage.py startapp ventas
```
Es necesario agregar la aplicación en el archivo settings.py

``` bash
INSTALLED_APPS = [
    'ventas',
    ...
]
```
Crear las migraciones
``` bash
python manage.py makemigrations
```
Aplicar las migraciones
``` bash
python manage.py migrate
```
Crear un super usuario
``` bash
python manage.py createsuperuser
```
Ejecutar el servidor
``` bash
python manage.py runserver
```
Crear un modelo
``` python
from django.db import models

class Cliente(models.Model):
    cédula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dirección = models.CharField(max_length=100)
    teléfono = models.IntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
class Producto(models.Model):
    código = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    número = models.IntegerField(primary_key=True)
    fecha = models.DateField(auto_now=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return str(self.número)
    
```
Registrar el modelo en el administrador
``` python
from django.contrib import admin
from .models import Pedido, Producto, Cliente

admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Cliente)
```
Aplicar Migraciones
``` bash
python manage.py makemigrations
```
``` bash
python manage.py migrate
```
Correr el Servidor
``` bash
python manage.py runserver
```
