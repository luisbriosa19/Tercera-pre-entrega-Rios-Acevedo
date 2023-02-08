from django.contrib import admin
from AppCoder.models import *

# Register your models here.

#Registro de modelos de nuestro proyecto
admin.site.register(Jugadores)
admin.site.register(Entrenadores)
admin.site.register(Deportes)
admin.site.register(Categorias)