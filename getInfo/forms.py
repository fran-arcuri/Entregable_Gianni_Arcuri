from django import forms

#Formularios

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    horasEstudio = forms.IntegerField()
    queEstudia = forms.CharField(max_length=30)

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    queEnsenia = forms.CharField(max_length=30)

class UniversidadForm(forms.Form):
    universidadDe = forms.CharField(max_length=30)
    aniosDeEstudio = forms.IntegerField()