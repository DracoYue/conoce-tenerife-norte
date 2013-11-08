from django.db import models
from django.contrib import admin
from django.forms import ModelForm
import datetime
# Create your models here.


class Municipio(models.Model):
    Nombre = models.CharField(max_length = 70)
    Latitud = models.BigIntegerField(max_length =  15)
    Longitud = models.BigIntegerField(max_length = 15)
    TlfA = models.IntegerField(max_length = 9)
    def __unicode__(self):
        return self.Nombre
    
class Senderos(models.Model):
    Nombre = models.CharField(max_length = 70)
    Latitud = models.BigIntegerField(max_length =  15)
    Longitud = models.BigIntegerField(max_length = 15)
    MuNom = models.ForeignKey(Municipio, related_name="sendero_municipio")
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
    Comentarios = models.CharField(max_length = 140)
    #Foto = models.ImafeField()

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
    
    
    
    
    