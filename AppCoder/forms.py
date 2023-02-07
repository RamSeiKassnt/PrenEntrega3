from django import forms 

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()
    comision = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class ProfesFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    edad = forms.IntegerField()
    
class EntregasFormulario(forms.Form):
    nombre = forms.CharField()
    fecha = forms.DateField()
    entregado = forms.BooleanField()