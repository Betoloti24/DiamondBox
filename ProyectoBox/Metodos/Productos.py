from Inventario.models import Producto, Material
from ProyectoBox.BD.Inventario import consultarProductos, consultarMaterialesProd, consultarMateriales

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
def listaMateriales():
    # Consultamos la lista de productos en la BD
    listaprod = consultarMateriales()
    lista = []

    # Creamos la lista de los productos
    for prod in listaprod:
        lista.append(Material(prod))

    return lista