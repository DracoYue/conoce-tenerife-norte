# Create your views here.
from contenido.models import *
from django.shortcuts import render_to_response
from django import forms
from django.shortcuts import render_to_response
from gmapi import maps
from gmapi.forms.widgets import GoogleMap
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

class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))


def mapa(request):
    gmap = maps.Map(opts = {
        'center': maps.LatLng(28.333395, -16.50238),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 9,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
    marker = maps.Marker(opts = {
        'map': gmap,
        'position': maps.LatLng(28.333395, -16.50238),
    })
    maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
    maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
    info = maps.InfoWindow({
        'content': 'Hello!',
        'disableAutoPan': True
    })
    info.open(gmap, marker)
    context = {'form': MapForm(initial={'map': gmap})}
    return render_to_response('senderos/mapa.html', context)

def senderos(request):
    gmap = maps.Map(opts = {
        'center': maps.LatLng(28.333395, -16.50238),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 9,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
    marker = maps.Marker(opts = {
        'map': gmap,
        'position': maps.LatLng(28.333395, -16.50238),
    })
    maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
    maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
    info = maps.InfoWindow({
        'content': 'Hello!',
        'disableAutoPan': True
    })
    info.open(gmap, marker)

    bbdd = Municipio.objects.all()
    municipio = []
    for i in bbdd:
        municipio.append(i)
    municipio.sort()

    context = {'form': MapForm(initial={'map': gmap}), 'municipio':municipio}
    return render_to_response('senderos/senderos.html', context)
    