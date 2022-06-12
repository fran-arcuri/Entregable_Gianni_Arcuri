from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from numpy import Inf
from requests import request
from .models import *
from .forms import *

# Create your views here.
def inicio(self):
    plantilla = loader.get_template("inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def estudiantes(self):
    plantilla = loader.get_template("estudiantes.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def profesores(self):
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def universidades(self):
    plantilla = loader.get_template("universidades.html")
    documento = plantilla.render()
    return HttpResponse(documento)

#Formularios
def estudiantesCrear(request):
    if request.method == "POST":
        miFormulario = EstudianteForm(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], horasEstudio=informacion['horasEstudio'], queEstudia=informacion['queEstudia'])
            estudiante.save()
            return render(request, "inicio.html")
    else:
        miFormulario = EstudianteForm()

    return render(request, "estudiantesForms.html", {'miFormulario':miFormulario})


def profesoresCrear(request):
    if request.method == "POST":
        miFormulario = ProfesorForm(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], queEnsenia=informacion['queEnsenia'])
            profesor.save()
            return render(request, "inicio.html")
    else:
        miFormulario = ProfesorForm()

    return render(request, "profesoresForms.html", {'miFormulario':miFormulario})

def universidadesCrear(request):
    if request.method == "POST":
        miFormulario = UniversidadForm(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            universidad = Universidad(universidadDe=informacion['universidadDe'], aniosDeEstudio=informacion['aniosDeEstudio'])
            universidad.save()
            return render(request, "inicio.html")
    else:
        miFormulario = UniversidadForm()

    return render(request, "universidadesForms.html", {'miFormulario':miFormulario})


#Busqueda
def buscarEstudiantes(request):
    return render(request, 'buscarEstudiantes.html')
    
def busquedaHoras(request):
    #respuesta = f"estoy buscando al estudiante con {request.GET['horas de estudio']} horas de estudio."
    if request.GET['horasEstudio']:
        horasEstudio = request.GET['horasEstudio']
        datos = Estudiante.objects.filter(horasEstudio=horasEstudio)
        return render(request, 'resultadosEstudiantes.html', {'datos':datos, 'horasEstudio':horasEstudio})
    else:
        respuesta = "no se ingreso ningun dato."
        return HttpResponse(respuesta)


def buscarProfesores(request):
    return render(request, 'buscarProfesores.html')
    
def busquedaMateria(request):
    #respuesta = f"estoy buscando al estudiante con {request.GET['horas de estudio']} horas de estudio."
    if request.GET['queEnsenia']:
        queEnsenia = request.GET['queEnsenia']
        datos = Profesor.objects.filter(queEnsenia=queEnsenia)
        return render(request, 'resultadosProfesores.html', {'datos':datos, 'queEnsenia':queEnsenia})
    else:
        respuesta = "no se ingreso ningun dato."
        return HttpResponse(respuesta)


def buscarUniversidades(request):
    return render(request, 'buscarUniversidades.html')
    
def busquedaAniosDeEstudio(request):
    #respuesta = f"estoy buscando al estudiante con {request.GET['horas de estudio']} horas de estudio."
    if request.GET['aniosDeEstudio']:
        aniosDeEstudio = request.GET['aniosDeEstudio']
        datos = Universidad.objects.filter(aniosDeEstudio=aniosDeEstudio)
        return render(request, 'resultadosUniversidades.html', {'datos':datos, 'aniosDeEstudio':aniosDeEstudio})
    else:
        respuesta = "no se ingreso ningun dato."
        return HttpResponse(respuesta)