from time import time
from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    horasEstudio = models.Charfield(time)
    queEstudia = models.CharField(max_length=30)

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    queEnsenia = models.CharField(max_length=30)

class Universidad(models.Model):
    universidadDe = models.CharField(max_length=30)
    aniosDeEstudio = models.IntegerField()