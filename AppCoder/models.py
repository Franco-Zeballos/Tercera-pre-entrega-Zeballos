from django.db import models

# Create your models here.
class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    camada =  models.IntegerField()
    cumple = models.DateField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=17)
    edad = models.IntegerField(default=0)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    comision = models.IntegerField()
    
class Familiar(models.Model):
    parentesco = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha = models.DateField()
    
    