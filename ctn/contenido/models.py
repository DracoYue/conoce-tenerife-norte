from django.db import models
from django.contrib import admin
from django.forms import ModelForm
import datetime
from django.contrib.auth.models import User
# Create your models here.


class Municipio(models.Model):
    Nombre = models.CharField(max_length = 70)
    Latitud = models.FloatField(max_length =  15)
    Longitud = models.FloatField(max_length = 15)
    TlfA = models.IntegerField(max_length = 9)
    def __unicode__(self):
        return self.Nombre
    
class Senderos(models.Model):
    Nombre = models.CharField(max_length = 70)
    Latitud = models.FloatField(max_length =  15)
    Longitud = models.FloatField(max_length = 15)
    NVotos = models.FloatField(max_length=15)
    puntos = models.FloatField(max_length=15)
    MuNom = models.ForeignKey(Municipio, related_name="MuNom")
    MUYBIEN = 'MB'
    BIEN = 'B'
    REGULAR = 'R'
    NORECOMENDABLE = 'NR'
    Calificacion = (
        (MUYBIEN, 'MB'),
         (BIEN, 'B'),
         (REGULAR, 'R'),
         (NORECOMENDABLE, 'NR'),
    )
    Puntuacion = models.CharField(max_length = 2,
                                choices = Calificacion,
                                default = MUYBIEN)
    Coordenadas = models.CharField(max_length = 6000)
    #LatitudD = models.CharField(max_length =  6000)
    
    
    def __unicode__(self):
        return self.Nombre
   
class Comentarios(models.Model):
    coment = models.CharField(max_length = 200)
    usuario = models.ForeignKey(User, related_name = "usuario")
    sendero = models.ForeignKey(Senderos, related_name = "sende")
    fecha = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-fecha']

    def __unicode__(self):
        return self.coment


class Fotos(models.Model):
    Imagen = models.ImageField(upload_to = 'static/img/subidas/')
    usuario = models.ForeignKey(User, related_name = "usuariof")
    sendero = models.ForeignKey(Senderos, related_name = "sendef")
    fecha = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-fecha']

    def __unicode__(self):
        return "%s: %s" % (self.Imagen, self.sendero)


    
class LugaresInteres(models.Model):
    Nombre = models.CharField(max_length = 70)
    MUSEO = 'MU'
    PLAYAS = 'PL'
    TEATRO = 'TE'
    CINE = 'CI'
    NATURALEZA = 'NA'
    EDIFICIOS = 'ED'
    Tipo =  (
        (MUSEO, 'MU'),
        (PLAYAS, 'PL'),
        (TEATRO, 'TE'),
        (CINE, 'CI'),
        (NATURALEZA, 'NA'),
        (EDIFICIOS, 'ED'),
    )
    Eleccion = models.CharField(max_length = 2,
                                choices = Tipo,
                                default = EDIFICIOS)
    Direccion = models.CharField(max_length = 70)
    MuNom = models.ForeignKey(Municipio, related_name="lugar_municipio")
    Tlf = models.IntegerField(max_length = 9)
    def __unicode__(self):
        return self.Nombre
    
class Actividades(models.Model):
    Nombre = models.CharField(max_length = 70)
    Lugar = models.CharField(max_length = 70)
   # Fecha = models.DataTimeField(auto_now_add = True)
    Coste = models.IntegerField(max_length = 3)
    INFANTIL = 'IN'
    ADULTO = 'AD'
    TODOS = 'TO'
    Tipo = (
        (INFANTIL, 'IN'),
        (ADULTO, 'AD'),
        (TODOS, 'TO'),
        )
    Eleccion = models.CharField(max_length = 2,
                                choices = Tipo,
                                default = TODOS)
    MuNom = models.ForeignKey(Municipio, related_name="actividad_municipio")
    
   # class Meta:
    #    ordering = ['-fecha']
        
    def __unicode__(self):
        return self.Nombre
    
    
    
    
    