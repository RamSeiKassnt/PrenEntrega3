from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def estudiantes(request):
    listaAlumnos=Estudiante.objects.all()
    return render(request, "AppCoder/verEstudiantes.html",{"listaAlumnos":listaAlumnos})

def profesores(request):
    listaProfes = Profesor.objects.all()
    return render(request, "AppCoder/verProfesores.html",{"listaProfes":listaProfes})

def entregables(request):
    listaEntregas = Entregable.objects.all()
    return render(request, "AppCoder/verEntregables.html",{"listaEntregas":listaEntregas})

def cursos(request):
    listaCursos = Curso.objects.all()
    return render(request, "AppCoder/verCursos.html",{"listaCursos":listaCursos})

# def crear_estudiantes(request): #crear form con HTML
    #if request.method=='POST':
     #   estudiante1= Estudiante(nombre=request.POST['nombre'],apellido=request.POST['apellido'],email=request.POST['email'])
      #  estudiante1.save()
       # return render(request, "AppCoder/inicio.html")
    #return render(request, "AppCoder/crear_estudiantes.html")

def crear_cursos(request): #crear form desde django
    if request.method == 'POST':
        miFormulario=CursoFormulario(request.POST)
        
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data
            
            curso1 = Curso(nombre=infoDic["nombre"], camada = infoDic["camada"], comision=infoDic["comision"])
            curso1.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario=CursoFormulario()
        
    return render(request, "AppCoder/crear_curso.html",{"formulario1":miFormulario})  

def nuevo_estudiante(request): #crear form desde django
    if request.method == 'POST':
        miFormulario=EstudianteFormulario(request.POST)
        
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data
            
            estudiante1 = Estudiante(nombre=infoDic["nombre"], apellido = infoDic["apellido"], email=infoDic["email"])
            estudiante1.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario=EstudianteFormulario()
        
    return render(request, "AppCoder/crear_estudiantes.html",{"formulario1":miFormulario})




def agregar_profe(request): #crear form desde django
    if request.method == 'POST':
        miFormulario=ProfesFormulario(request.POST)
        
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data
            
            profe1 = Profesor(nombre=infoDic["nombre"], apellido = infoDic["apellido"], email=infoDic["email"], profesion=infoDic["profesion"], edad=infoDic["edad"])
            profe1.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario=ProfesFormulario()
        
    return render(request, "AppCoder/agregar_profe.html",{"formulario1":miFormulario})



def nueva_entrega(request): #crear form desde django
    if request.method == 'POST':
        miFormulario=EntregasFormulario(request.POST)
        
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data
            
            entrega1 = Entregable(nombre=infoDic["nombre"], fecha = infoDic["fecha"], entregado=infoDic["entregado"])
            entrega1.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario=EntregasFormulario()
        
    return render(request, "AppCoder/crear_curso.html",{"formulario1":miFormulario})

def busquedaCamada(request):
    return render(request, "Appcoder/busquedaCamada.html")

def resultadosBusqueda(request):
    if request.method == "GET":
        camadaBusqueda = request.GET["camada"]
        cursosResultados = Curso.objects.filter(camada__icontains=camadaBusqueda)
        
        return render(request, "AppCoder/resultadosBusqueda.html", {"camada":camadaBusqueda, "resultado":cursosResultados})    
    return render(request, "AppCoder/resultadosBusqueda.html")

