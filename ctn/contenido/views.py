# Create your views here.
from contenido.models import *
from django.shortcuts import render_to_response

def listar_municipio(request):
    bbdd = Municipio.objects.all()
    municipio = []
    for i in bbdd:
        municipio.append(i.Nombre)
    municipio.sort()
    return render_to_response('senderos/senderos.html',{'municipio':municipio})
    