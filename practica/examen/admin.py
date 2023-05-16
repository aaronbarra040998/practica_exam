from django.contrib import admin

# Importamos los modelos Pregunta y Opcion del archivo models.py
from .models import Pregunta, Opcion

# Registramos los modelos en el panel de administración
admin.site.register(Pregunta)
admin.site.register(Opcion)
