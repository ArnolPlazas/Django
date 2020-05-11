from django.http import HttpResponse
from django.template import Template, Context
#from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render

import datetime


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):
    #documento = '<html><body><h1>Hola alumnos esta es la primera pagina con Django</h1></body></html>'
    documento = """
        <html>
            <body>
                <h1>Hola alumnos esta es la primera pagina con Django</h1>
            </body>
        </html>"""

    return HttpResponse(documento)


def despedida(request):
    return HttpResponse('Hasta luego alumnos de Django')

def darFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
        <html>
            <body>
                Fecha y hora actuales %s
            </body>
        </html>""" % fecha_actual
    return HttpResponse(documento)


def calculaEdad(request, agno, edad):
    #edadActual = 30
    periodo = agno - 2020
    #edadFutura = edadActual + periodo
    edadFutura = edad + periodo
    documento = """
        <html>
            <body>
                <h2>En el año %s tendrás %s años</h2>
            </body>
        </html>""" % (agno, edadFutura)

    return HttpResponse(documento)


def saludo_plantilla(request):

    doc_externo = open('C:/Users/arnol/OneDrive/Documents/Documentos/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html')
    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)

    return HttpResponse(documento)

def saludo_plantilla2(request):
    #nombre = 'Arnol'
    #apellido = 'Plazas'
    ahora = datetime.datetime.now()

    p1 = Persona("Mathieu", "Plazas")

    doc_externo = open('C:/Users/arnol/OneDrive/Documents/Documentos/ProyectosDjango/Proyecto1/Proyecto1/plantillas/plantillaVariable.html')
    plt = Template(doc_externo.read())

    doc_externo.close()

    #ctx = Context({"nombre_persona": nombre, "apellido_persona": apellido, "fecha": ahora})
    ctx = Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "fecha": ahora, "temas": ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]})
    
    
    documento = plt.render(ctx)

    return HttpResponse(documento)

def saludo_plantilla3(request):
    ahora = datetime.datetime.now()
    p1 = Persona("Mathieu", "Plazas") 
    temas_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    #doc_externo = loader.get_template('plantillaVariable.html')
    doc_externo = get_template('plantillaVariable.html') 
    documento = doc_externo.render({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "fecha": ahora, "temas": temas_curso})

    return HttpResponse(documento)


def saludo_plantilla4(request):
    ahora = datetime.datetime.now()
    p1 = Persona("Mathieu", "Plazas") 
    temas_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    return render(request, "plantillaVariable.html", {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "fecha": ahora, "temas": temas_curso})


def curso(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "CursoC.html", {"dameFecha": fecha_actual})

def cursoDjango(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "CursoDjango.html", {"dameFecha": fecha_actual})