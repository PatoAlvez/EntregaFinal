from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre= models.CharField(max_length=25)
    telefono=models.CharField(max_length=12)
    fecha_de_nacimiento=models.DateField()
    email=models.EmailField(max_length=25)
