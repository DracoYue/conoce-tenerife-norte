from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.views.generic import *
from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ctn.views.home', name='home'),
    # url(r'^ctn/', include('ctn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    #url(r'^private/',  'usuario.views.mostrar_perfil'),
    url(r'^private/',  TemplateView.as_view(template_name="perfil.html")),
    url(r'^login/$', TemplateView.as_view(template_name="register.html")),
    url(r'^logout/$','usuario.views.logout'),
    url(r'^$', TemplateView.as_view(template_name="static_pages/index.html")),
    url(r'^contact/', TemplateView.as_view(template_name="static_pages/contact.html")),
    url(r'^about/', TemplateView.as_view(template_name="static_pages/about.html")),
    url(r'^help/', TemplateView.as_view(template_name="static_pages/help.html")),
    #url(r'^rutas/', 'contenido.views.municipio'),
  
    url(r'^senderos/', 'contenido.views.municipio'),
    #url(r'^caldera/', TemplateView.as_view(template_name="senderos/caldera.html")),
)
