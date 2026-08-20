from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Página inicial de la primarapp del Proyecto</h1>")


def ahora(request):
    hora = datetime.datetime.now()
    salida = f"<b>Fecha y hora actual: {hora}</b>"
    return HttpResponse(salida)

def inacap(request):
    return HttpResponse("<a href='https://www.inacap.cl/' target='_blank'>Ir a la página de Inacap</a>")

