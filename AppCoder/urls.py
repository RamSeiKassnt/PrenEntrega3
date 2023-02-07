from django.urls import path
from AppCoder.views import * 

urlpatterns = [
    path('inicio/', inicio, name='Start'),
    path('ver_estudiantes/', estudiantes, name="Alumnos"),
    path('ver_profes/', profesores, name="Profes"),
    path('ver_entregables/', entregables, name="Entregas"),
    path('ver_cursos/', cursos, name="Trainings"),
    
    path('crear_estudiantes/', nuevo_estudiante, name="Nuevo Estudiante"),
    path('crear_curso/', crear_cursos, name="Nuevo Curso"),
    path('agregar_profe/', agregar_profe, name="Nuevo Profe"),
    path('nueva_entrega/', nueva_entrega, name="Nueva Entrega"),

    path('buscar_camada/', busquedaCamada, name="Buscar Camada"),
    path('resultados_busqueda/', resultadosBusqueda), 
]