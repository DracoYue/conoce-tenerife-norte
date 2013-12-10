from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.views.generic import *
from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^$', 'contenido.views.index'),
    url(r'^private/', 'contenido.views.perfil'),
    url(r'^logout/$','usuario.views.logout'),
    url(r'^contact/', 'contenido.views.contact'),
    url(r'^about/', 'contenido.views.about'),
    url(r'^help/', 'contenido.views.help'),
    url(r'^municipios/$', 'contenido.views.municipio2'),
    url(r'^municipios/(\d+)/$', 'contenido.views.municipio3'),
    url(r'^senderos/$', 'contenido.views.municipio'),
    url(r'^senderos/(\d+)/$', 'contenido.views.senderos'),
    url(r'^actividades/$', 'contenido.views.municipio4'),
    url(r'^actividades/(\d+)/$', 'contenido.views.actividades2'),
    url(r'^votos/(\d+)/(\d+)/$','contenido.views.votos'),
    url(r'^login/$', 'contenido.views.login'),
    url(r'^fotos/(\d+)/$','contenido.views.fotos'),
    url(r'^foto_borrar/(\d+)/$','contenido.views.borrar_fotos'),
    url(r'^comentarios/(\d+)/$', 'contenido.views.comentarios'),
    url(r'^comentarios_borrar/(\d+)/$', 'contenido.views.borrar_comentarios'),


)
