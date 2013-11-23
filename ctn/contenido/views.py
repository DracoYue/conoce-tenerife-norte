# Create your views here.
from contenido.models import *
from django.shortcuts import render_to_response
from django import forms
from django.shortcuts import render_to_response

def listar_sendero(request, numero):
    bbdd = Municipio.objects.all()
    municipio = []
    for i in bbdd:
        municipio.append(i)
    municipio.sort()

    numero = int(numero)
    #numero = Municipio.objects.get(Nombre=nombre).id
    senderos = []
    n_senderos = Senderos.objects.count()
    for i in range(1,n_senderos+1) :
        print numero
        print Senderos.objects.get(id=i).MuNom_id
        if (numero == Senderos.objects.get(id=i).MuNom_id):
            senderos.append(Senderos.objects.get(id=i).Nombre)
    senderos.sort()

    
    return render_to_response('senderos/rutas.html',{'senderos':senderos, 'municipio':municipio})   



def municipio(request):
   

    bbdd = Municipio.objects.all()
    municipio = []
    for i in bbdd:
        municipio.append(i)
    municipio.sort()

    context = {'municipio':municipio}
    return render_to_response('senderos/senderos.html', context)
    