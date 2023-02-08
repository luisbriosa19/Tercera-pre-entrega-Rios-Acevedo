from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

#Creamos el vinculo de nuestro templates a las vistas de nuesta app.
def inicio(request):
    return render(request,"AppCoder\inicio.html")

def jugador(request):
    return render(request,"AppCoder\jugadores.html")

def entrenador(request):
    return render(request,"AppCoder\entrenadores.html")

def categoria(request):
    return render(request,"AppCoder\categorias.html")

#crear un formulario usando django
def crear_jugador(request): #formulario carga de datos del models Jugadores
    if request.method == 'POST': # al hacer click a enviar: se van a guardar los datos y crearse el curso en la BD.
        form_Jugadores = JugadoresFormulario(request.POST)
        if form_Jugadores.is_valid(): #validacion de datos
            jugadoresdicc = form_Jugadores.cleaned_data #convertir la informacion a informacion tipo diccionario.
            jugador1 = Jugadores(nombre = jugadoresdicc["nombre"], apellido = jugadoresdicc["apellido"], edad = jugadoresdicc["edad"], deporte = jugadoresdicc["deporte"], )
            jugador1.save() #guardamos la informacion del diccionario.
            return render(request, "AppCoder/Inicio.html") #Vinculo a la pagina de Inicio de nuestro template.
    else: #si no le doy click en enviar debo mostrar el formulario vacio
        form_Jugadores = JugadoresFormulario()
    return render(request, "AppCoder/jugadores.html", {"formjugadores1":form_Jugadores})

def crear_entrenador(request): #formulario carga de datos del models Entrenadores
    if request.method == 'POST': # al hacer click a enviar: se van a guardar los datos y crearse el curso en la BD.
        form_Entrenadores = EntrenadoresFormulario(request.POST)
        if form_Entrenadores.is_valid(): #validacion de datos.
            entrenadoresdicc = form_Entrenadores.cleaned_data #convertir la informacion a informacion tipo diccionario.
            entrenador1 = Entrenadores(nombre = entrenadoresdicc["nombre"], apellido = entrenadoresdicc["apellido"], email = entrenadoresdicc["email"], deporte = entrenadoresdicc["deporte"], )
            entrenador1.save() #guardamos la informacion del diccionario.
            return render(request, "AppCoder/Inicio.html") #Vinculo a la pagina de Inicio de nuestro template.
    else: #si no le doy click en enviar debo mostrar el formulario vacio
        form_Entrenadores = EntrenadoresFormulario()
    return render(request, "AppCoder/entrenadores.html", {"formentrenadores1":form_Entrenadores})

def crear_deporte(request): #formulario carga de datos del models Deportes
    if request.method == 'POST': # al hacer click a enviar: se van a guardar los datos y crearse el curso en la BD.
        form_Deportes = DeportesFormulario(request.POST)
        if form_Deportes.is_valid(): #validacion de datos.
            deportesDicc = form_Deportes.cleaned_data #convertir la informacion a informacion tipo diccionario.
            deportes1 = Deportes(nombre = deportesDicc["nombre"], grupo = deportesDicc["grupo"])
            deportes1.save()  #guardamos la informacion del diccionario.
            return render(request, "AppCoder/Inicio.html") #Vinculo a la pagina de Inicio de nuestro template.
    else: #si no le doy click en enviar debo mostrar el formulario vacio
        form_Deportes = DeportesFormulario()
    return render(request, "AppCoder/deportes.html", {"formDeportes1":form_Deportes})

def crear_categoria(request): #formulario carga de datos del models Categorias
    if request.method == 'POST': # al hacer click a enviar: se van a guardar los datos y crearse el curso en la BD.
        form_Categorias = CategoriasFormulario(request.POST)
        if form_Categorias.is_valid(): #validacion de datos.
            categoriasDicc = form_Categorias.cleaned_data #convertir la informacion a informacion tipo diccionario.
            categorias1 = Categorias(nombre = categoriasDicc["nombre"], genero = categoriasDicc["genero"])
            categorias1.save() #guardamos la informacion del diccionario.
            return render(request, "AppCoder/Inicio.html") #Vinculo a la pagina de Inicio de nuestro template.
    else: #si no le doy click en enviar debo mostrar el formulario vacio
        form_Categorias = CategoriasFormulario()
    return render(request, "AppCoder/categorias.html", {"formCategorias1":form_Categorias})

#Vista de busqueda en nuestra BD.
def busqueda_deporte(request):
    return render(request, "AppCoder/inicio.html")

#Vista de resultados de datos solicitados.
def resultado_deporte(request):
    if request.GET["grupo"]:
        grupo = request.GET["grupo"]
        deportes = Deportes.objects.filter(grupo__iexact=grupo)
        return render(request, "AppCoder/inicio.html", {"deportes":deportes, "grupo":grupo}) 
    else:
        respuesta = "No enviaste datos."
    return HttpResponse(respuesta)