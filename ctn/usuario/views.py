#encoding: utf-8

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages

from social_auth import __version__ as version
from usuario.models import *

from social_auth.backends.google import GoogleOAuth2Backend

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/login/')


