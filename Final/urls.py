from django.urls import path
from .views import *




urlpatterns = [
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("agregarEstudiante/", agregarEstudiantes, name="agregarEstudiante"),
    
    

    
    
    path("agregarProfesores/", agregarProfesores, name="agregarProfesores"),
    path("profesores/", leerProfesores, name="profesores"),

   
]