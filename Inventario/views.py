from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from ProyectoBox.Metodos.Productos import *
from ProyectoBox.BD.Inventario import *
from django.core.files.storage import FileSystemStorage
from os import remove

# Vista del inventario
def inventario(request):
    # Validamos que se haya hecho una sesión
    usuario = request.COOKIES.get("usuario", False)
    print(request.COOKIES)
    if (usuario):
        # Variables de error
        elimM = False
        elimexit = False
        obj, nombobj, tipooper = "", "", ""
        # Verificamos si se posee algun metodo del request
        if (request.method == "POST"):
            if (request.POST["accion"] == "modificarM"):
                cod = request.POST["codigo"]
                url = str(reverse_lazy("modificarM", kwargs = {"codigo":cod}))
                http = HttpResponseRedirect(url)
                return http
            elif (request.POST["accion"] == "modificarP"):
                cod = request.POST["codigo"]
                url = str(reverse_lazy("modificarP", kwargs = {"codigo":cod}))
                http = HttpResponseRedirect(url)
                return http
            elif (request.POST["accion"] == "eliminarP"):
                cod = request.POST["codigo"]
                objeto = consultarProducto(cod)
                if (objeto):
                    ruta = objeto.imagen[3:]
                    remove(ruta)
                    eliminarProducto(cod)
                    elimexit = True
                    obj = "producto"
                    nombobj = objeto.nombre
                    tipooper = "eliminado"
            elif (request.POST["accion"] == "eliminarM"):
                cod = request.POST["codigo"]
                if (consultarComposicion(cod) == True):
                    objeto = consultarMaterial(cod)
                    if (objeto):
                        ruta = objeto.imagen[3:]
                        remove(ruta)
                        eliminarMaterial(cod)
                        elimexit = True
                        obj = "material"
                        tipooper = "eliminado"
                        nombobj = objeto.nombre
                else:
                    elimM = True
            elif (request.POST["accion"] == "cerrar"):
                url = str(reverse_lazy("logeo"))
                http = HttpResponseRedirect(url)
                http.delete_cookie("usuario")
                return http

        # Extraer datos de sesion
        producto = request.COOKIES.get("Pmodificacion", None)
        pmod = False
        nombre = ""
        tipo = ""
        operacion = ""
        if (producto):
            nombre = request.COOKIES["Producto"]
            pmod = True
            tipo = request.COOKIES["Tipo"]
            operacion = request.COOKIES["Operacion"]
            del request.COOKIES["Pmodificacion"]
            del request.COOKIES["Producto"]
            del request.COOKIES["Tipo"]
            del request.COOKIES["Operacion"]

        # Declaramos el contexto
        contexto = {
            "productos": listaProductos(),
            "materiales": listaMateriales(),
            "errormaterial": elimM,
            "pnombre": nombre,
            "pmod": pmod,
            "tipo": tipo,
            "operacion": operacion,
            "elimexit": elimexit,
            "objeto": obj,
            "nombobj": nombobj,
            "tipooper": tipooper
        }

        # Renderizar pagina    
        return render(request, 'inventario.html', contexto)
    else:
        url = str(reverse_lazy("logeo"))
        http = HttpResponseRedirect(url)
        return http

# Vista de Agregar Material
def agregarMaterial(request):
    # Validamos que se haya hecho una sesión
    usuario = request.COOKIES.get("usuario", False)
    if (usuario):
        # Variables de error
        errorDato = False
        # Verificamos si se obtiene un metodo en el request
        if (request.method == "POST"):
            print(request.POST)
            if ("cerrar" in request.POST):
                url = str(reverse_lazy("logeo"))
                http = HttpResponseRedirect(url)
                http.delete_cookie("usuario")
                return http
            else:
                nombre = request.POST["nombre"]
                corte = request.POST["corte"]
                precio = request.POST["precio"]
                pais = request.POST["pais"]
                descripcion = request.POST["descripcion"]
                cantidad = request.POST["cantidad"]
                if (len(descripcion) == 0 or pais == "off"):
                    errorDato = True
                else:
                    if (corte == "off"):
                        corte = "NULL"
                    if (pais == "off"):
                        pais = "NULL"
                    # Datos de la imagen
                    myfile = request.FILES['archivo']               
                    imagen = nombre.replace(" ", "").lower()
                    extencion = str(myfile).split(".")[1]
                    nombreimagen = f"{imagen}.{extencion}"   
                    # Guardamos el archivo
                    fs = FileSystemStorage()
                    fs.location += "\\Materiales"                   
                    # Salvamos el archivo con el nombre deseado
                    filename = fs.save(f"{nombreimagen}", myfile)    
                    # Ingresamos el archivo guardad
                    uploaded_file_url = fs.url(filename)
                    # Ingresamos el material
                    ingresarMaterial(nombre, descripcion, precio, corte, pais, cantidad, nombreimagen)
                    url = str(reverse_lazy("inventario"))
                    http = HttpResponseRedirect(url)
                    # Asiganmos una variable de confirmacion al diccionario de sesion
                    http.set_cookie("Pmodificacion", True)
                    http.set_cookie("Producto", nombre)
                    http.set_cookie("Tipo", "material")
                    http.set_cookie("Operacion", "creado")
                    return http

        # Creamos el contexto
        contexto = {
            "paises": listaPaises(),
            "errorDato": errorDato,
        }

        return render(request, 'agregarMaterial.html', contexto)
    else:
        url = str(reverse_lazy("logeo"))
        http = HttpResponseRedirect(url)
        return http

# Vista de Agregar Producto
def agregarProducto(request):
    # Validamos que se haya hecho una sesión
    usuario = request.COOKIES.get("usuario", False)
    if (usuario):
        # Variables de error
        errorDato = False
        # Verificamos si se obtiene un metodo en el request
        if (request.method == "POST"):
            if ("cerrar" in request.POST):
                url = str(reverse_lazy("logeo"))
                http = HttpResponseRedirect(url)
                http.delete_cookie("usuario")
                return http
            nombre = request.POST["nombre"]
            categoria = request.POST["categoria"]
            precio = request.POST["precio"]
            cantidad = request.POST["cantidad"]     
            # Validamos que haya algun material seleccionado
            materiales = False
            for llave in request.POST:
                if (llave[0] == "M"):
                    materiales = True
            # Verificamos que no haya ningun error
            if (categoria == "off" or materiales == False):
                errorDato = True
            else:
                # Datos de la imagen
                myfile = request.FILES['archivo']               
                imagen = nombre.replace(" ", "").lower()
                extencion = str(myfile).split(".")[1]
                nombreimagen = f"{imagen}.{extencion}"   
                # Guardamos el archivo
                fs = FileSystemStorage()
                fs.location += "\\Productos"                   
                # Salvamos el archivo con el nombre deseado
                filename = fs.save(f"{nombreimagen}", myfile)    
                # Ingresamos el archivo guardad
                uploaded_file_url = fs.url(filename)   
                # Buscamos los materiales
                materiales = []
                for llave in request.POST:
                    if (llave[0] == "M"):
                        materiales.append(int(llave[1:]))
                # Actualizar el producto
                ingresarProducto(nombre, precio, categoria, materiales, cantidad, nombreimagen)
                url = str(reverse_lazy("inventario"))
                http = HttpResponseRedirect(url)
                # Asiganmos una variable de confirmacion al diccionario de sesion
                http.set_cookie("Pmodificacion", True)
                http.set_cookie("Producto", nombre)
                http.set_cookie("Tipo", "producto")
                http.set_cookie("Operacion", "creado")
                return http

        # Creamos el contexto
        contexto = {
            "materiales": listaMateriales(),
            "errorDato": errorDato,
        }

        return render(request, 'agregarProducto.html', contexto)
    else:
        url = str(reverse_lazy("logeo"))
        http = HttpResponseRedirect(url)
        return http

# Vista de Consultar
def consultar(request):
    # Validamos que se haya hecho una sesión
    usuario = request.COOKIES.get("usuario", False)
    if (usuario):
        # Variables de decision y de error
        producto, material = [False, False]
        errorObj = False
        objeto = None

        # Verificamos si se obtiene un metodo post
        if (request.method == "POST"):
            if ("cerrar" in request.POST):
                url = str(reverse_lazy("logeo"))
                http = HttpResponseRedirect(url)
                http.delete_cookie("usuario")
                return http
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
    else:
        url = str(reverse_lazy("logeo"))
        http = HttpResponseRedirect(url)
        return http

# Vista de Modificar Material
def modificarMaterial(request, codigo):
    # Validamos que se haya hecho una sesión
    usuario = request.COOKIES.get("usuario", False)
    if (usuario):
        # Variables de error
        errorDato = False
        # Verificamos si se obtiene un metodo en el request
        if (request.method == "POST"):
            if ("cerrar" in request.POST):
                url = str(reverse_lazy("logeo"))
                http = HttpResponseRedirect(url)
                http.delete_cookie("usuario")
                return http
            nombre = request.POST["nombre"]
            corte = request.POST["corte"]
            precio = request.POST["precio"]
            pais = request.POST["pais"]
            descripcion = request.POST["descripcion"]
            cantidad = request.POST["cantidad"]
            # Antiguos datos
            objeto = consultarMaterial(codigo)
            antiguaimagen = objeto.imagen[3:]
            antiguonombre = objeto.nombre
            # Validación
            if (len(descripcion) == 0 or pais == "off"):
                errorDato = True
            else:
                if (corte == "off"):
                    corte = "NULL"
                if (pais == "off"):
                    pais = "NULL"
                try:
                    # Datos de la imagen
                    myfile = request.FILES['archivo']               
                    imagen = nombre.replace(" ", "").lower()
                    extencion = str(myfile).split(".")[1]
                    nombreimagen = f"{imagen}.{extencion}"   
                    # Guardamos el archivo
                    fs = FileSystemStorage()
                    fs.location += "\\Materiales"                   
                    # Eliminamos el archivo antiguo 
                    remove(antiguaimagen)
                    # Salvamos el archivo con el nombre deseado
                    filename = fs.save(f"{nombreimagen}", myfile)    
                    # Ingresamos el archivo guardad
                    uploaded_file_url = fs.url(filename)
                except:
                    nombreimagen = None 
                # Actualizamos los datos
                updateMaterial(codigo, nombre, descripcion, precio, corte, pais, cantidad, nombreimagen)
                url = str(reverse_lazy("inventario"))
                http = HttpResponseRedirect(url)
                # Asiganmos una variable de confirmacion al diccionario de sesion
                http.set_cookie("Pmodificacion", True)
                http.set_cookie("Producto", antiguonombre)
                http.set_cookie("Tipo", "material")
                http.set_cookie("Operacion", "actualizado")
                return http

        # Creamos el contexto
        contexto = {
            "material": consultarMaterial(codigo),
            "paises": listaPaises(),
            "errorDato": errorDato,
        }

        return render(request, 'modificarMaterial.html', contexto)
    else:
        url = str(reverse_lazy("logeo"))
        http = HttpResponseRedirect(url)
        return http

# Vista de Modificar Producto
def modificarProducto(request, codigo):
    # Validamos que se haya hecho una sesión
    usuario = request.COOKIES.get("usuario", False)
    if (usuario):
        # Variables de error
        errorDato = False
        # Verificamos si se obtiene un metodo en el request
        if (request.method == "POST"):
            if ("cerrar" in request.POST):
                url = str(reverse_lazy("logeo"))
                http = HttpResponseRedirect(url)
                http.delete_cookie("usuario")
                return http
            nombre = request.POST["nombre"]
            categoria = request.POST["categoria"]
            precio = request.POST["precio"]
            cantidad = request.POST["cantidad"]
            # Antiguos datos
            objeto = consultarProducto(codigo)
            antiguaimagen = objeto.imagen[3:]
            antiguonombre = objeto.nombre
            # Validamos que haya algun material seleccionado
            materiales = False
            for llave in request.POST:
                if (llave[0] == "M"):
                    materiales = True
            # Verificamos que no haya ningun error
            if (categoria == "off" or materiales == False):
                errorDato = True
            else:
                try:
                    # Datos de la imagen
                    myfile = request.FILES['archivo']               
                    imagen = nombre.replace(" ", "").lower()
                    extencion = str(myfile).split(".")[1]
                    nombreimagen = f"{imagen}.{extencion}"   
                    # Guardamos el archivo
                    fs = FileSystemStorage()
                    fs.location += "\\Productos"                   
                    # Eliminamos el archivo antiguo 
                    remove(antiguaimagen)
                    # Salvamos el archivo con el nombre deseado
                    filename = fs.save(f"{nombreimagen}", myfile)    
                    # Ingresamos el archivo guardad
                    uploaded_file_url = fs.url(filename) 
                except:
                    nombreimagen = None                
                # Buscamos los materiales
                materiales = []
                for llave in request.POST:
                    if (llave[0] == "M"):
                        materiales.append(int(llave[1:]))
                # Actualizar el producto
                updateProducto(codigo, nombre, precio, categoria, materiales, cantidad, nombreimagen)
                url = str(reverse_lazy("inventario"))
                http = HttpResponseRedirect(url)
                # Asiganmos una variable de confirmacion al diccionario de sesion
                http.set_cookie("Pmodificacion", True)
                http.set_cookie("Producto", antiguonombre)
                http.set_cookie("Tipo", "producto")
                http.set_cookie("Operacion", "actualizado")
                return http

        # Creamos el contexto
        consulta = consultarMaterialesProd(codigo)

        check = listaMaterialesProd(consulta)
        contexto = {
            "producto": consultarProducto(codigo),
            "materiales": listaMateriales(checks = check),
            "check": check,
            "errorDato": errorDato,
        }

        return render(request, 'modificarProducto.html', contexto)
    else:
        url = str(reverse_lazy("logeo"))
        http = HttpResponseRedirect(url)
        return http
        