from django.shortcuts import render
from .models import Estudiantes, Profesores, Entregable
from Final.forms import EstudiantesForm, ProfesoresForm, EntregableForm
from django.http import HttpResponse




# Create your views here.



#-----------------------BLOQUE ESTUDIANTES ---------------------------
def estudiantes(request):
    return render(request, 'templatesFinal/estudiantes.html')

def leerEstudiantes(request):
    estudiantes = Estudiantes.objects.all()
    return render (request, 'templatesFinal/estudiantes.html', {'estudiantes': estudiantes})

def busquedaEstudiantes(request):
    return render(request, 'templatesFinal/busquedaEstudiante.html')
    
# ------ NO ME SALIO EL BUSCAR -------

"""def buscar(request):
    estudiantes = request.GET["estudiante"]
    if estudiantes!= "":
        estudiantes = Estudiantes.objects.filter(estudiante__icontains=estudiantes)
        return render(request, 'templatesFinal/resultadosBusqueda.html', {'estudiantes': estudiantes})
    else:
        return render(request, 'templatesFinal/busquedaEstudiantes.html', {'estudiante': "No has ingresado un estudiante para buscar"})
"""


def agregarEstudiantes(request):
    if request.method == 'POST':
        form = EstudiantesForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            curso = info['curso']
            dni = info['dni']
            estudiante = Estudiantes( nombre = nombre, apellido = apellido, curso = curso, dni = dni)
            estudiante.save()
            estudiante = Estudiantes.objects.all()
            return render(request, 'templatesFinal/estudiantes.html', {'estudiantes': estudiante, 'mensaje': "Estudiante guardado correctamente" })
        else:
            return render(request, 'templatesFinal/agregarEstudiante.html', {'form': form, 'mensaje': "Ocurrio un error" })

    else: 
        form= EstudiantesForm()
        return  render(request, 'templatesFinal/agregarEstudiante.html', {'form': form})



#------------------------BLOQUE PROFESORES ---------------------------
def leerProfesores(request):
    profesores = Profesores.objects.all()
    return render(request, 'templatesFinal/profesores.html', {'profesor': profesores})
    

def agregarProfesores(request):
    if request.method == 'POST':
        form = ProfesoresForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            comision = info['comision']
            profesor =  Profesores(nombre = nombre, apellido = apellido, comision = comision)
            profesor.save()
            profesor = Profesores.objects.all()
            return render(request, 'templatesFinal/profesores.html', {'profesores': profesor})
        else:
            return render(request, 'templatesFinal/agregarProfesores.html', {'form': form})

    else: 
        form= ProfesoresForm()
        return  render(request, 'templatesFinal/agregarProfesores.html', {'form': form})



            
