from django.db import models

# Create your models here.

# Definición del modelo Pregunta
class Pregunta(models.Model):
    # Campo para almacenar el texto de la pregunta
    Pregunta_text = models.CharField(max_length=200)
    
    # Campo para almacenar la fecha de publicación
    pub_date = models.DateTimeField('date published')

    # Método para representar la pregunta como una cadena
    def __str__(self):
        return self.Pregunta_text

# Definición del modelo Opcion
class Opcion(models.Model):
    # Campo para almacenar la pregunta relacionada con la opción (clave externa)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    # Campo para almacenar el texto de la opción
    opcion_text = models.CharField(max_length=200)

    # Campo para almacenar los puntos asociados a la opción
    puntos = models.IntegerField(default=0)

    # Método para representar la opción como una cadena
    def __str__(self):
        return self.opcion_text
