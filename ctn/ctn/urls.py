from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.views.generic import *


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
    url(r'^private/',  TemplateView.as_view(template_name="dentro.html")),
    url(r'^login/$', TemplateView.as_view(template_name="register.html")),
    url(r'^logout/$','usuario.views.logout'),
)
