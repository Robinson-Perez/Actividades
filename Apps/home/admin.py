from django.contrib import admin
from .models import Comentario, Estudiante, Administradores, Articulo

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Administradores)
admin.site.register(Articulo)
admin.site.register(Comentario)