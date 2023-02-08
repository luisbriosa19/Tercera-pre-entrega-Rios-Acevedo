from django import forms
#formularios creados. 
class JugadoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    deporte = forms.CharField(max_length=40)

class EntrenadoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    deporte = forms.CharField(max_length=40)

class DeportesFormulario(forms.Form):    
    nombre = forms.CharField(max_length=40)
    grupo = forms.IntegerField()

class CategoriasFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)