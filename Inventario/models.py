from django.db import models

# Clase Material
class Material():
    def __init__(self, *args):
        parametros = args[0]
        self.cod = parametros[0]
        self.nombre = parametros[1]
        self.descripcion = parametros[2]
        self.precio = parametros[3]
        self.imagen = f"../static/img/Materiales/{parametros[4]}"
        self.corte = parametros[5]
        self.origen = str(parametros[6])
        self.position = 0

    # Metodos get
    def getcod (self):
        return self.cod
    def getnombre (self):
        return self.nombre

    # Metodos set
    def setposition (self, position):
        self.position = position

# Clase Producto
class Producto ():
    # Constructor
    def __init__(self, *args):
        parametros = args[0]
        self.cod = parametros[0]
        self.nombre = parametros[1]
        self.precio = parametros[2]
        self.categoria = parametros[3]
        self.imagen = f"../static/img/Productos/{parametros[4]}"
        self.materiales = []
        self.position = 0
    
    # Metodos get
    def getcod (self):
        return self.cod
    def getnombre (self):
        return self.nombre
    def getprecio (self):
        return self.precio
    def getimagen (self):
        return self.imagen
    def getcategoria (self):
        return self.categoria
    def getmateriales (self):
        return self.materiales

    # Metodos set
    def setposition (self, position):
        self.position = position

    # Metodo para ingresar un nuevo material
    def addMaterial (self, material):
        self.materiales.append(material)

# Clase Paises
class Pais():
    def __init__(self, *args):
        parametros = args[0]
        self.cod = parametros[0]
        self.nombre = parametros[1]
    