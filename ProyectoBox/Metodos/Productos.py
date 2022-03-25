from msilib.schema import CheckBox
from Inventario.models import Pais, Producto, Material
from ProyectoBox.BD.Inventario import *

# Metodo para crear la lista de productos
def listaProductos():
    # Consultamos la lista de productos en la BD
    listaprod = consultarProductos()
    lista = []

    # Creamos la lista de los productos
    for prod in listaprod:
        lista.append(Producto(prod))

    # Asignar los materiales de un producto
    for prod in lista:
        # Extraer materiales
        materiales = consultarMaterialesProd(prod.getcod())

        # Asignamos materiales
        for material in materiales:
            prod.addMaterial(Material(material))

    return lista

# Metodo para crear la lista de materiales
def listaMateriales(**kwars):
    # Consultamos la lista de productos en la BD
    listaprod = consultarMateriales()
    lista = []

    # Creamos la lista de los productos
    check = kwars.get("checks", None)
    if (check):
        for prod in listaprod:
            if prod[0] in check:
                lista.insert(0, Material(prod))
            else:
                lista.append(Material(prod))
    else:
        for prod in listaprod:
            lista.append(Material(prod))

    return lista

# Metodo para crear la lista de paises
def listaPaises():
    # Consultamos la lista de paises en la BD
    listaprod = consultarPaises()
    lista = []

    # Creamos la lista de los paises
    for prod in listaprod:
        lista.append(Pais(prod))

    return lista

# Metodo para crear la lista de materiales
def listaMaterialesProd(materiales):
    # Consultamos la lista de materiales en la BD
    lista = []

    # Creamos la lista de los materiales
    for material in materiales:
        m = Material(material)
        lista.append(m.getcod())

    return lista

