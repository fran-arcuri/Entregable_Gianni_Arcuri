from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def inicio(self):
    plantilla = loader.get_template("inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def estudiantes(self):
    test = "pagina de estudiantes"
    return HttpResponse(test)

def profesores(self):
    test = "pagina de profesores"
    return HttpResponse(test)

def universidades(self):
    test = "pagina de universidades"
    return HttpResponse(test)