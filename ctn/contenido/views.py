# Create your views here.
from contenido.models import *
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from contenido.forms import *
from django.shortcuts import render_to_response, render
from django.template import RequestContext


def municipio(request):
    bbdd = Municipio.objects.all()
    bbdd2 = Senderos.objects.all()
    senderos = []
    municipio = []
    usu_autenticado = request.user.is_authenticated()

    for i in bbdd:
        municipio.append(i)

    for i in bbdd2:
        senderos.append(i)

    context = {'municipio':municipio, 'senderos':senderos, 'usu_autenticado':usu_autenticado}
    return render_to_response('senderos/senderos.html', context)

def municipio2(request):
    bbdd = Municipio.objects.all()
    
    municipio2 = []
    
    usu_autenticado = request.user.is_authenticated()
    for i in bbdd:
        municipio2.append(i)

    context = {'municipio2':municipio2,'usu_autenticado':usu_autenticado}
    return render_to_response('municipios/municipios.html', context)

def municipio3(request, n_municipio):
    
    bbdd = LugaresInteres.objects.all()
    municipio = Municipio.objects.get(id=n_municipio)
    usu_autenticado = request.user.is_authenticated()
    nid = n_municipio
    nombre = municipio.Nombre
    latitud = municipio.Latitud
    longitud = municipio.Longitud
    telefono = municipio.TlfA
    lugar = []


    for i in bbdd:
        if i.MuNom_id == int(nid):
            lugar.append(i)
    print lugar
            

    context = {'nid':nid,'nombre':nombre, 'latitud':latitud, 'longitud':longitud, 'tlfa':telefono, 'lugar':lugar, 'usu_autenticado':usu_autenticado}
    
    return render_to_response('municipios/municipios_info.html', context)
    
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
    
    usu_autenticado = request.user.is_authenticated()
    if request.user.is_authenticated():
        mensaje = 'Aun no han calificado este sendero'
        sendero = Senderos.objects.get(id=nid)
        if (sendero.NVotos > 0):
            resultado = sendero.puntos/sendero.NVotos 
            print resultado
            if resultado == 1:
                mensaje = 'No Recomendado'
            elif resultado == 2:
                mensaje = 'Regular'
            elif resultado == 3:
                mensaje = 'Bien'
            else :
                mensaje = 'Muy Bien'
    else:
        mensaje = 'Si deseas opinar, Registrate!'

    form_comen = Coment(request.POST)
    form_foto = Foto(request.POST, request.FILES)



    bbdd = Fotos.objects.all()
    bbdd2 = Comentarios.objects.all()
    fotos = []
    comentarios = []
    rutas = []

    for i in range(0, len(bbdd)):
        print bbdd[i].sendero.Nombre
        print Senderos.objects.get(id=n_sendero)
        if(bbdd[i].sendero.Nombre == Senderos.objects.get(id=n_sendero).Nombre):
            fotos.append(bbdd[i])
        else:
            print "distintos"


    for i in range(0, len(bbdd2)):
        print bbdd2[i].sendero.Nombre
        print Senderos.objects.get(id=n_sendero)
        if(bbdd2[i].sendero.Nombre == Senderos.objects.get(id=n_sendero).Nombre):
            comentarios.append(bbdd2[i])
        else:
            print "distinto"

        

    for i in fotos:
        rutas.append('src=../../%s' %i.Imagen)
        


    context = {'fotos':fotos, 'comentarios':comentarios, 'rutas':rutas,'usu_autenticado':usu_autenticado,'form_foto': form_foto,'form_comen': form_comen, 'mensaje':mensaje,'nid':nid,'nombre':nombre, 'latitud':latitud, 'longitud':longitud, 'municipio':municipio, 'puntos':puntos, 'coordenadas':coordenadas}

    
    return render_to_response('senderos/senderos_info.html', context, RequestContext(request))


def votos(request, voto, sid):
    
    if request.user.is_authenticated():
        voto = int(voto)
        sendero = Senderos.objects.get(id=sid)
        sendero.puntos = voto+sendero.puntos
        sendero.NVotos = 1 + sendero.NVotos
        

        print sendero.puntos
        print sendero.NVotos
        sendero.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print "ERROR autentiquese"
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def comentarios(request, sid):
    if request.method == 'POST':
        form_comen = Coment(request.POST)
        if form_comen.is_valid():
            comentario = Comentarios()
            comentario.coment = form_comen.cleaned_data['Coment']
            comentario.sendero_id = sid
            comentario.usuario_id = request.user.id
            comentario.save()
            return HttpResponseRedirect('/senderos/'+sid+'/')
        else:
            form_comen = Coment()
            return render_to_response('senderos_info.html', {'form_comen':form_comen}, RequestContext(request))
    else:
        print "No funciona"
        return HttpResponseRedirect('/')

def borrar_comentarios(request, comentario_id):
    comen = Comentarios.objects.get(id = comentario_id)
    comen.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    
def municipio4(request):
    bbdd = Municipio.objects.all()
    bbdd2 = Actividades.objects.all()
    actividades = []
    municipio4 = []
    usu_autenticado = request.user.is_authenticated()
    
    for i in bbdd:
        municipio4.append(i)

    for i in bbdd2:
        actividades.append(i)

    context = {'municipio4':municipio4, 'actividades':actividades, 'usu_autenticado':usu_autenticado}
    return render_to_response('actividades/actividades.html', context)


def actividades2(request, n_actividades):
    
    actividades = Actividades.objects.get(id=n_actividades)
    nid = n_actividades
    nombre = actividades.Nombre
    lugar = actividades.Lugar
    coste = actividades.Coste
    eleccion = actividades.Eleccion
    munnom = actividades.MuNom
    usu_autenticado = request.user.is_authenticated()

    context = {'nid':nid,'nombre':nombre, 'lugar':lugar, 'coste':coste, 'eleccion':eleccion,'usu_autenticado':usu_autenticado}
    
    return render_to_response('actividades/actividades_info.html', context)

def index(request):
    usu_autenticado = request.user.is_authenticated()
    return render_to_response('static_pages/index.html', {'usu_autenticado':usu_autenticado})

def contact(request):
    usu_autenticado = request.user.is_authenticated()
    return render_to_response('static_pages/contact.html', {'usu_autenticado':usu_autenticado})

def about(request):
    usu_autenticado = request.user.is_authenticated()
    return render_to_response('static_pages/about.html', {'usu_autenticado':usu_autenticado})

def help(request):
    usu_autenticado = request.user.is_authenticated()
    return render_to_response('static_pages/help.html', {'usu_autenticado':usu_autenticado})

def login(request):
    usu_autenticado = request.user.is_authenticated()
    return render_to_response('register.html', {'usu_autenticado':usu_autenticado})

def perfil(request):
    usu_autenticado = request.user.is_authenticated()
    user = User.objects.get(id = request.user.id)
    
    bbdd = Fotos.objects.all()
    bbdd2 = Comentarios.objects.all()
    fotos = []
    comentarios = []
    rutas = []
    nombre_imagen = []

    for i in range(0, len(bbdd)):
        print bbdd[i].usuario.username
        print User.objects.get(id=request.user.id)
        if(bbdd[i].usuario.username == User.objects.get(id=request.user.id).username):
            fotos.append(bbdd[i])
        else:
            print "distintos"


    for i in range(0, len(bbdd2)):
        print bbdd2[i].usuario.username
        print User.objects.get(id=request.user.id)
        if(bbdd2[i].usuario.username == User.objects.get(id=request.user.id).username):
            comentarios.append(bbdd2[i])
        else:
            print "distintos"

    
    for i in fotos:
        rutas.append('src=../%s' %i.Imagen)



    return render_to_response('perfil.html', {'rutas':rutas, 'usu_autenticado':usu_autenticado, 'user':user, 'fotos':fotos, 'comentarios':comentarios})


def fotos(request, sid):
     if request.method == 'POST':
        form_foto = Foto(request.POST, request.FILES)

        if form_foto.is_valid():
            print "formulario valido"
            
            imagen = Fotos()
            imagen.Imagen = form_foto.cleaned_data['imagen']
            print imagen.Imagen
            nombre = str(imagen.Imagen)
            imagen.sendero_id = sid
            imagen.usuario_id = request.user.id
            if (Fotos.objects.filter(Imagen = 'static/img/subidas/' + nombre)):
                print "ya se ha subido una imagen con ese nombre "
            else:
                imagen.save()

            print request.META.get('HTTP_REFERER')
            return HttpResponseRedirect('/senderos/'+sid+'/')
        else:
            print "esto se va "
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    
def borrar_fotos(request,foto_id):
    foto = Fotos.objects.get(id = foto_id)
    foto.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

