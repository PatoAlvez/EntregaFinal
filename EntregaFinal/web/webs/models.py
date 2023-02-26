from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre= models.CharField(max_length=25)
    telefono=models.CharField(max_length=12)
    fecha_de_nacimiento=models.DateField()
    email=models.EmailField(max_length=25)

class Juegos(models.Model):
     nombre= models.CharField(max_length=25)
     categoria= models.CharField(max_length=25)
     empresa= models.CharField(max_length=25)
     cantidad=models.DateField

     def __str__(self):
        return f"Nombre:{self.nombre} - Categoria: {self.categoria}- Empresa: {self.empresa}- Cantidad: {self.cantidad}"
