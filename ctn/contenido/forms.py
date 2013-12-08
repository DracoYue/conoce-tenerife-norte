from django.forms import *
from contenido.models import *
from django import forms

class Coment(forms.Form):
	Coment = forms.CharField(max_length=200, label='Comentar')  

class Foto(forms.Form):
	imagen = forms.ImageField(label='Imagen')
