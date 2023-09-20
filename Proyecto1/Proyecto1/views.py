from django.http import HttpResponse
import datetime
def saludo(request): #primera vista
    documento="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>titulo</title>
        <!-- favicon -->
        <!-- estilos -->

    </head>
    <body>
    <h1>Hola mundo</h1>
        <!-- header -->
        <!-- nav -->

        
        
        <!-- favicon -->

        <!-- favicon -->

    </body>
    </html>
    """
    return HttpResponse(documento)

def despedida(request): #primera vista
    return HttpResponse("Adios")

def fecha(request):
    fecha_actual = datetime.datetime.now()
    documento="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>titulo</title>
        <!-- favicon -->
        <!-- estilos -->

    </head>
    <body>
    <h1>Fecha y hora actuales {} </h1>
        <!-- header -->
        <!-- nav -->

        
        
        <!-- favicon -->

        <!-- favicon -->

    </body>
    </html>
    """.format(fecha_actual)
    return HttpResponse(documento)


def calculaEdad(request,edad,agno):
    periodo=agno -1995
    edadfutura=edad+periodo
    documento=f"<h2>en el año {agno} tendras {edadfutura} años"
    return HttpResponse(documento)

