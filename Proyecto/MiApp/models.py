from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    comision = models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre}, Comision: {self.comision}'

class Instructor(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Correo: {self.email}, Profesion: {self.profesion}'

class Alumnos(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='images/', null=True, blank=True)