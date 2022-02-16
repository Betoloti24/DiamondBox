from mysql.connector import connect

# Funcion para consultar la lista de productos
def consultarProductos():
    # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    DML = f"SELECT p.* FROM proyectobox.productos p ORDER BY p.cod"
    cursor.execute(DML)
    lista = cursor.fetchall()

    # Cerrar conexion
    conexion.close()

    # Creamos la lista de objetos tipo productos

    return lista

# Funcion para consultar e insertar los materiales de los productos
def consultarMaterialesProd(cod):
    # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    DML = f"SELECT pm.cod, pm.nombre, pm.descripcion, pm.precio, pm.imagen, pm.corte, pp.nombre as origen FROM proyectobox.materiales pm LEFT JOIN proyectobox.paises pp on pm.origen = pp.cod LEFT JOIN proyectobox.p_m ppm on pm.cod = ppm.cod_material WHERE ppm.cod_producto = {cod}"
    cursor.execute(DML)
    lista = cursor.fetchall()

    # Cerrar conexion
    conexion.close()

    # Creamos la lista de objetos tipo productos

    return lista

# Funcion para consultar e insertar los materiales 
def consultarMateriales():
    # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    DML = f"SELECT pm.cod, pm.nombre, pm.descripcion, pm.precio, pm.imagen, pm.corte, pp.nombre as origen FROM proyectobox.materiales pm LEFT JOIN proyectobox.paises pp on pm.origen = pp.cod"
    cursor.execute(DML)
    lista = cursor.fetchall()

    # Cerrar conexion
    conexion.close()

    # Creamos la lista de objetos tipo productos

    return lista