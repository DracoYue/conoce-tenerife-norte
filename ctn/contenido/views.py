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
    