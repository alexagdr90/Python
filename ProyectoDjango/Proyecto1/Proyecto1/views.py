from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render 
class Persona(object):

    def __init__(self,nombre,apellido):

        self.nombre = nombre
        self.apellido =apellido



def saludo(request): # primera vista

    p1=Persona("Profesor Alejandro","Gomez")
    #nombre ="Alejandro"
    #apellido ="Gomez"
    temas_del_curso=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    ahora=datetime.datetime.now()


   # doc_externo=open("C:/Users/Alex/Documents/ejercicios python/ProyectoDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    #plt=Template(doc_externo.read())

   # doc_externo.close()

    #doc_externo=get_template('miplantilla.html')

    #ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas": temas_del_curso})

   # documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas": temas_del_curso})

    return render(request, "miplantilla.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas": temas_del_curso})

def cursoC(request):
    fecha_actual=datetime.datetime.now()
    
    return render(request, "CursoC.html", {"dameFecha":fecha_actual})

def cursoCss(request):
    fecha_actual=datetime.datetime.now()
    
    return render(request, "cursoCss.html", {"dameFecha":fecha_actual})



def despedida(request):

    return HttpResponse("Hasta luego")


def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>"""% fecha_actual

    return HttpResponse(documento)

    
def calculaEdad(request, edad, agno):

    #edadActual=18
    periodo=agno-2019
    edadFutura=edad+periodo

    documento="<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)
    return HttpResponse(documento)


