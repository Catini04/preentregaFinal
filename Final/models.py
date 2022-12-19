from django.db import models

# Create your models here.


class Estudiantes(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    dni = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"




class Profesores(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    comision = models.IntegerField()



class Entregable(models.Model):
    Nombre_estudiantes = models.CharField(max_length=100)
    Entregable = models.BooleanField()


