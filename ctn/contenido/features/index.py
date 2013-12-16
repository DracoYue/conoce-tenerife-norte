from lettuce import *
from lxml import html
from nose.tools import assert_equals
from contenido.models import *
from django.test.client import Client

##################################################################3
#Scenario: Probar el acceso al HTML raiz
@before.all
def set_browser():
    world.browser = Client()
    
@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'Then I see the first link "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[0]
    assert header.text == text

@step(r'Then I see the second link "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[1]
    assert header.text == text

@step(r'Then I see the third link "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[2]
    assert header.text == text

@step(r'Then I see the fourth link "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[3]
    assert header.text == text

@step(r'I see the header "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("title")[0]
    assert header.text == text

@step(r'I see the a "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[5]
    assert header.text == text

###############################################################
#Scenario: Probar el acceso a help

@step(r'Then I see h1 "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("h1")[0]
    assert header.text == text

@step(r'Then I see the first h4 "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("h4")[0]
    assert header.text == text

@step(r'Then I see the first h5 "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("h5")[0]
    assert header.text == text

###############################################################
#Scenario: Probar el acceso a contacto
@step(r'Then I see the first p "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("p")[0]
    assert header.text == text

##########################################################
#Scenario: Probar el acceso a municipios
@step(r'Then I see the eighth a "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[7]
    assert header.text == text

@step(r'Then I see the ninth a "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[8]
    assert header.text == text

@step(r'Then I see the tenth a "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[9]
    assert header.text == text

@step(r'Then I see the eleventh a "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[10]
    assert header.text == text

@step(r'Then I see the twelfth a "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[11]
    assert header.text == text

@step(r'Then I see the thirteenth a "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[12]
    assert header.text == text

@step(r'Then I see the fourteenth a "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[13]
    assert header.text == text

@step(r'Then I see the fifteenth a "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("a")[14]
    assert header.text == text

###################################################
#Scenario: Probar el acceso a senderos
@step(r'Then I see the first h3 "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect("h3")[0]
    assert header.text == text