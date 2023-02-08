from django.urls import path
from AppCoder.views import *

#urls de nuestra aplicacion por cada vista creada.
urlpatterns = [
    path("", inicio, name="Inicio"),
    path("jugadores/", crear_jugador, name="Jugador"),
    path("entrenadores/", crear_entrenador, name="Entrenador"),
    path("deportes/", crear_deporte, name="Deporte"),
    path("categorias/", crear_categoria, name="Categoria"),

    #url de busqueda de datos.
    path("resultado_deporte/", resultado_deporte, name="ResultadosDeporte"),    
]
