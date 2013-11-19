# Create your views here.
from contenido.models import *
from django.shortcuts import render_to_response

def listar_municipio(request):
    bbdd = Municipio.objects.all()
    bbdd2 = Senderos.objects.all()
    municipio = []
    senderos = []
    for i in bbdd:
        municipio.append(i.Nombre)
    municipio.sort()
    for i in bbdd2:
        senderos.append(i.Nombre)
    senderos.sort()
    return render_to_response('senderos/senderos.html',{'municipio':municipio, 'senderos':senderos})
    

    