from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return HttpResponse(
        "<h1>Página inicial de la segundapp del Proyecto"
    )

def saludo(request):
    salida = "<h1>Buenas tardes desde segundapp"
    return HttpResponse(salida)

