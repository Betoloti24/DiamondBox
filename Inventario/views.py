from configparser import NoSectionError
from multiprocessing import context
from pickle import FALSE, TRUE
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from ProyectoBox.Metodos.Productos import *
from ProyectoBox.BD.Inventario import *

# Vista del inventario
def inventario(request):
    # Variables de error
    elimM = False
    # Verificamos si se posee algun metodo del request
    if (request.method == "POST"):
        if (request.POST["accion"] == "agregarM"):
            url = str(reverse_lazy("agregarM"))
            http = HttpResponseRedirect(url)
            return http
        elif (request.POST["accion"] == "agregarP"):
            url = str(reverse_lazy("agregarP"))
            http = HttpResponseRedirect(url)
            return http
        elif (request.POST["accion"] == "consultar"):
            url = str(reverse_lazy("consultar"))
            http = HttpResponseRedirect(url)
            return http
        elif (request.POST["accion"] == "modificarM"):
            cod = request.POST["codigo"]
            url = str(reverse_lazy("modificarM", kwargs = {"codigo":cod}))
            http = HttpResponseRedirect(url)
            return http
        elif (request.POST["accion"] == "modificarP"):
            cod = request.POST["codigo"]
            url = str(reverse_lazy("modificarP", kwargs = {"codigo":cod}))
            http = HttpResponseRedirect(url)
            return http
        elif (request.POST["accion"] == "consultar"):
            url = str(reverse_lazy("consultar"))
            http = HttpResponseRedirect(url)
            return http
        elif (request.POST["accion"] == "eliminarP"):
            cod = request.POST["codigo"]
            eliminarProducto(cod)
        elif (request.POST["accion"] == "eliminarM"):
            cod = request.POST["codigo"]
            if (consultarComposicion(cod) == True):
                eliminarMaterial(cod)
            else:
                elimM = True

    # Declaramos el contexto
    contexto = {
        "productos": listaProductos(),
        "materiales": listaMateriales(),
        "errormaterial": elimM,
    }

    # Renderizar pagina    
    return render(request, 'inventario.html', contexto)

# Vista de Agregar Material
def agregarMaterial(request):
    # Variables de error
    errorDato = False
    # Verificamos si se obtiene un metodo en el request
    if (request.method == "POST"):
        nombre = request.POST["nombre"]
        corte = request.POST["corte"]
        precio = request.POST["precio"]
        pais = request.POST["pais"]
        descripcion = request.POST["descripcion"]
        if (len(descripcion) == 0 or corte == "off" or pais == "off"):
            errorDato = True
        else:
            ingresarMaterial(nombre, descripcion, precio, corte, pais)
            url = str(reverse_lazy("inventario"))
            http = HttpResponseRedirect(url)
            return http

    # Creamos el contexto
    contexto = {
        "paises": listaPaises(),
        "errorDato": errorDato,
    }

    return render(request, 'agregarMaterial.html', contexto)

# Vista de Agregar Producto
def agregarProducto(request):
    # Variables de error
    errorDato = False
    # Verificamos si se obtiene un metodo en el request
    if (request.method == "POST"):
        nombre = request.POST["nombre"]
        categoria = request.POST["categoria"]
        precio = request.POST["precio"]
        # Validamos que haya algun material seleccionado
        materiales = False
        for llave in request.POST:
            if (llave[0] == "M"):
                materiales = True
        # Verificamos que no haya ningun error
        if (categoria == "off" or materiales == False):
            errorDato = True
        else:
            # Buscamos los materiales
            materiales = []
            for llave in request.POST:
                if (llave[0] == "M"):
                    materiales.append(int(llave[1:]))
            print(materiales)
            # Actualizar el producto
            ingresarProducto(nombre, precio, categoria, materiales)
            url = str(reverse_lazy("inventario"))
            http = HttpResponseRedirect(url)
            return http

    # Creamos el contexto
    contexto = {
        "materiales": listaMateriales(),
        "errorDato": errorDato,
    }

    return render(request, 'agregarProducto.html', contexto)

# Vista de Consultar
def consultar(request):
    # Variables de decision y de error
    producto, material = [False, False]
    errorObj = False
    objeto = None

    # Verificamos si se obtiene un metodo post
    if (request.method == "POST"):
        codigo = request.POST["codigo"]
        tipo = request.POST["tipo"]
        if (tipo == "PRODUCTO"):
            objeto = consultarProducto(codigo)
            if (objeto != None):
                producto = True
            else:
                errorObj = True
        elif (tipo == "MATERIAL"):
            objeto = consultarMaterial(codigo)
            if (objeto != None):
                material = True
            else:
                errorObj = True 
    # Creamos el contexto
    contexto = {
        "objeto": objeto,
        "material": material,
        "producto": producto,
        "errorObj": errorObj,
    }
    return render(request, 'consultar.html', contexto)

# Vista de Modificar Material
def modificarMaterial(request, codigo):
    # Variables de error
    errorDato = False
    # Verificamos si se obtiene un metodo en el request
    if (request.method == "POST"):
        nombre = request.POST["nombre"]
        corte = request.POST["corte"]
        precio = request.POST["precio"]
        pais = request.POST["pais"]
        descripcion = request.POST["descripcion"]
        if (len(descripcion) == 0 or corte == "off" or pais == "off"):
            errorDato = True
        else:
            updateMaterial(codigo, nombre, descripcion, precio, corte, pais)
            url = str(reverse_lazy("inventario"))
            http = HttpResponseRedirect(url)
            return http

    # Creamos el contexto
    contexto = {
        "material": consultarMaterial(codigo),
        "paises": listaPaises(),
        "errorDato": errorDato,
    }

    return render(request, 'modificarMaterial.html', contexto)

# Vista de Modificar Producto
def modificarProducto(request, codigo):
    # Variables de error
    errorDato = False
    # Verificamos si se obtiene un metodo en el request
    if (request.method == "POST"):
        nombre = request.POST["nombre"]
        categoria = request.POST["categoria"]
        precio = request.POST["precio"]
        # Validamos que haya algun material seleccionado
        materiales = False
        for llave in request.POST:
            if (llave[0] == "M"):
                materiales = True
        # Verificamos que no haya ningun error
        if (categoria == "off" or materiales == False):
            errorDato = True
        else:
            # Buscamos los materiales
            materiales = []
            for llave in request.POST:
                if (llave[0] == "M"):
                    materiales.append(int(llave[1:]))
            print(materiales)
            # Actualizar el producto
            updateProducto(codigo, nombre, precio, categoria, materiales)
            url = str(reverse_lazy("inventario"))
            http = HttpResponseRedirect(url)
            return http

    # Creamos el contexto
    consulta = consultarMaterialesProd(codigo)

    contexto = {
        "producto": consultarProducto(codigo),
        "materiales": listaMateriales(),
        "check": listaMaterialesProd(consulta),
        "errorDato": errorDato,
    }

    return render(request, 'modificarProducto.html', contexto)