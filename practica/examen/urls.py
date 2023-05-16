from django.urls import path

# Importamos las vistas definidas en el archivo views.py
from .import views

# Definimos un espacio de nombres para las URL de esta aplicación
app_name = "examen"

# Configuramos las URL de la aplicación
urlpatterns = [
    # Ruta principal, se mapea a la vista "index" en el archivo views.py
    path('', views.index, name='index'),
    path('resolver',views.resolver,name='resolver')
]
