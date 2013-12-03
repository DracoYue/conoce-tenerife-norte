# Create your views here.
from contenido.models import *
from django.shortcuts import render_to_response
from django import forms
from django.shortcuts import render_to_response

def municipio(request):
    bbdd = Municipio.objects.all()
    bbdd2 = Senderos.objects.all()
    senderos = []
    municipio = []

    for i in bbdd:
        municipio.append(i)

    for i in bbdd2:
        senderos.append(i)

    context = {'municipio':municipio, 'senderos':senderos}
    return render_to_response('senderos/senderos.html', context)
    
def senderos(request, n_sendero):
    
    sendero = Senderos.objects.get(id=n_sendero)
    nid = n_sendero
    nombre = sendero.Nombre
    latitud = sendero.Latitud
    longitud = sendero.Longitud
    municipio = sendero.MuNom
    puntos = sendero.Puntuacion
    aux = sendero.Coordenadas.split(',')
    coordenadas = []
    for i in aux:
        coordenadas.append(float(i))
    print len(coordenadas)
    

    context = {'nid':nid,'nombre':nombre, 'latitud':latitud, 'longitud':longitud, 'municipio':municipio, 'puntos':puntos, 'coordenadas':coordenadas}
    
    return render_to_response('senderos/senderos_info.html', context)