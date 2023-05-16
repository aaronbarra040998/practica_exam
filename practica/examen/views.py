from django.shortcuts import render

# Importamos los modelos Opcion y Pregunta del archivo models.py
from .models import Opcion,Pregunta

# Vista principal "index"
def index(request):
    # Obtener todas las preguntas de la base de datos
    lista_preguntas = Pregunta.objects.all()
    
    # Definir el contexto con las preguntas obtenidas
    context = {
        'preguntas': lista_preguntas
    }
    
    # Renderizar la plantilla 'index.html' con el contexto
    return render(request, 'index.html', context)
def resolver(request):
    preguntas=Pregunta.objects.all()
    nota=0
    for pregunta in preguntas:
        nota+=int(request.POST['pregunta_'+str(pregunta.id)])
        
    context={
        'nota':nota
    }
    
    return render (request,'resultados.html',context)
