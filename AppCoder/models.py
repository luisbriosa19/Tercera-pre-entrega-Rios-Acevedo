from django.db import models

# Create your models here.
#modelos usados en el proyecto. 
class Jugadores(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    deporte = models.CharField(max_length=40)

class Entrenadores(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    deporte = models.CharField(max_length=40)

class Deportes(models.Model):

    nombre = models.CharField(max_length=40)
    grupo = models.IntegerField()

class Categorias(models.Model):

    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)