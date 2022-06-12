from django.urls import path
from getInfo.views import *


urlpatterns = [
    #Paginas Principales
    path('', inicio),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('universidades/', universidades),
    #Formularios
    path('estudiantes/formulario/', estudiantesCrear, name='estudiantesCrear'),
    path('profesores/formulario/', profesoresCrear, name='profesoresCrear'),
    path('universidades/formulario/', universidadesCrear, name='universidadesCrear'),
    #Busqueda
    path('estudiantes/buscar/', buscarEstudiantes, name='buscarEstudiantes'),
    path('estudiantes/resultados/', busquedaHoras, name='resultadosEstudiantes'),

    path('profesores/buscar/', buscarProfesores, name='buscarProfesores'),
    path('profesores/resultados/', busquedaMateria, name='resultadosProfesores'),

    path('universidades/buscar/', buscarUniversidades, name='buscarUniversidades'),
    path('universidades/resultados/', busquedaAniosDeEstudio, name='resultadosUniversidades'),
]