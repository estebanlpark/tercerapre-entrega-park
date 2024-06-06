from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.
def curso(req, nombre, camada):

    nuevoCurso = curso(nombre=nombre, camada=camada)
    nuevoCurso.save()

    return HttpResponse(f"""
        <p>curso: {nuevoCurso.nombre} - camada: {nuevoCurso.camada} creado!</p>
    """)

def listaCurso(req):
    lista = curso.objects.all()

    return render(req, "listaCurso.html", {'listaCurso': lista})