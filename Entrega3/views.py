from django.http import HttpResponse
from django.template import Template, Context

def saludo(req):

    return HttpResponse("Hola mundo")

def saludo2(req):

    return HttpResponse(
        """
        <h1>Bienvenidos a mi primera Web</h1>
        <br>
        <br>
        <p>Esto es un saludo </p>
        """

    )

def saludoConNombre(req, name, lastName):

    docTexto=f"Mi nombre es: <br>{name} {lastName}"

    return HttpResponse(docTexto)
    

def probandoTemplate(req):

    miHtml = open("Entrega3/templates/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)