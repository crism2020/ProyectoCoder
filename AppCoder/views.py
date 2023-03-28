from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso



def curso(self, nombre, camada):
    curso=Curso(nombre=nombre, camada=camada)
    curso.save()
    documentoDeTexto=f"---Curso: {curso.nombre}  Camada: {curso.camada} creado!"

    return HttpResponse(documentoDeTexto)
