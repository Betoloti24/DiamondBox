from django.shortcuts import render
from ProyectoBox.BD.Logeo import consultarusuario, ingresarusuario, validarusuario
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
# Vista de logeo
def logeo(request):
    # Declaracion de variables
    ErrorUsuario = False
    # Verificamos si se ha enviado un metodo post
    if (request.method == "POST"):
        # Extraemos los datos
        usuario = request.POST["usuario"]
        clave = request.POST["clave"]
        # Verificamos si el usuario existe
        if (consultarusuario(usuario, clave) == True):
            url = str(reverse_lazy("inventario"))
            http = HttpResponseRedirect(url)
            return http
        else:
            ErrorUsuario = True

    # Declaramos el Contexto
    contexto = {
        "ErrorUsuario": ErrorUsuario,
    }

    print(ErrorUsuario)

    return render(request, 'logeo.html', contexto)

# Vista de registro
def registro(request):
    # Declaracion de variables
    Error = False
    Mensaje = ""
    if (request.method == "POST"):
        # Extraemos los datos
        usuario = request.POST["usuario"]
        clave = request.POST["clave"]
        codacceso = request.POST["cseguridad"]

        # Verificamos que se haya ingresado bien el codigo de seguridad
        if (codacceso == '2357'):
            # Verificamos si el usuario existe
            if (validarusuario(usuario) == False):
                ingresarusuario(usuario, clave)
                url = str(reverse_lazy("inventario"))
                http = HttpResponseRedirect(url)
                return http
            else:
                Error = True
                Mensaje = f"¡¡ERROR!!, el usuario '{usuario}' ya está registrado en la base de datos, vuelva a intentar con otro usuario."
        else:
            Error = True
            Mensaje = f"¡¡ERROR!!, la clave de segurodad ingresada no es válida, comuníquese con el administrador y vuelva a intentar."

    # Definir el contexto
    contexto = {
        "Error": Error,
        "Mensaje": Mensaje,
    }
    
    return render(request, 'registro.html', contexto)