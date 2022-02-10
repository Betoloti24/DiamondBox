from django.shortcuts import render
from ProyectoBox.BD.Logeo import consultarusuario, ingresarusuario, validarusuario
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
# Vista de logeo
def logeo(request):
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
            print(f"No existe")

    return render(request, 'logeo.html')

# Vista de registro
def registro(request):
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
                print(f"El usuario ya existe")
        else:
            print(f"Clave de seguridad no valida")

    return render(request, 'registro.html')