from django import forms



class EstudiantesForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    curso = forms.CharField(label='Curso')
    dni = forms.IntegerField(label='DNI')


class ProfesoresForm(forms.Form):
    nombre = forms.CharField(label='Nombre profe')
    apellido = forms.CharField(label='Apellido profe')
    comision = forms.IntegerField(label='Nº Comision')


class EntregableForm(forms.Form):
    pass