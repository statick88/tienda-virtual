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