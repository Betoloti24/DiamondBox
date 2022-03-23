from mysql.connector import connect
from Inventario.models import Material, Producto

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
    DML = f"SELECT pm.cod, pm.nombre, pm.descripcion, pm.precio, pm.imagen, pm.corte, pm.cantidad, pp.nombre as origen FROM proyectobox.materiales pm LEFT JOIN proyectobox.paises pp on pm.origen = pp.cod LEFT JOIN proyectobox.p_m ppm on pm.cod = ppm.cod_material WHERE ppm.cod_producto = {cod}"
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
    DML = f"SELECT pm.cod, pm.nombre, pm.descripcion, pm.precio, pm.imagen, pm.corte, pm.cantidad, pp.nombre as origen FROM proyectobox.materiales pm LEFT JOIN proyectobox.paises pp on pm.origen = pp.cod"
    cursor.execute(DML)
    lista = cursor.fetchall()

    # Cerrar conexion
    conexion.close()

    return lista

# Funcion para determinar si el material esta siendo usado en un producto
def consultarComposicion(material):
    # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    DML = f"SELECT * FROM proyectobox.p_m ppm WHERE ppm.cod_material = {material}"
    cursor.execute(DML)
    validacion = cursor.fetchall()

    # Cerrar conexion
    conexion.close()

    return len(validacion) == 0

# Funcion para eliminar un material
def eliminarMaterial(cod):
    # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    DML = f"DELETE FROM proyectobox.materiales pp WHERE pp.cod = {cod};"
    cursor.execute(DML)

    # Hacer permanente los cambios y cerrar conexion
    conexion.commit()
    conexion.close()
    
# Funcion para eliminar un producto
def eliminarProducto(cod):
    # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    DML = f"DELETE FROM proyectobox.p_m ppm WHERE ppm.cod_producto = {cod};"
    cursor.execute(DML)

    DML = f"DELETE FROM proyectobox.productos pp WHERE pp.cod = {cod};"
    cursor.execute(DML)

    # Hacer permanente los cambios y cerrar conexion
    conexion.commit()
    conexion.close()

# Funcion para consultar un producto
def consultarProducto(cod):
    # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    DML = f"SELECT * FROM proyectobox.productos WHERE cod = {cod}"
    cursor.execute(DML)

    objeto = cursor.fetchall()
    if (len(objeto) != 0):
        objeto = Producto(objeto[0])

        # Creamos la lista de materiales
        materiales = consultarMaterialesProd(cod)

        # Asignamos materiales
        for material in materiales:
            objeto.addMaterial(Material(material))
    else:
        objeto = None

    # Hacer permanente los cambios y cerrar conexion
    conexion.close()

    return objeto

# Consultar material
def consultarMaterial(cod):
    # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    DML = f"SELECT pm.cod, pm.nombre, pm.descripcion, pm.precio, pm.imagen, pm.corte, pm.cantidad, pp.nombre as origen  FROM proyectobox.materiales pm LEFT JOIN proyectobox.paises pp on pm.origen = pp.cod WHERE pm.cod = {cod}"
    cursor.execute(DML)

    objeto = cursor.fetchall()
    if (len(objeto) != 0):
        objeto = Material(objeto[0])
    else:
        objeto = None

    print(f"{objeto}--{cod}")
    # Hacer permanente los cambios y cerrar conexion
    conexion.close()

    return objeto

# Modificar material
def updateMaterial(cod, nombre, descripcion, precio, corte, origen, cantidad):
     # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    DML = f"UPDATE proyectobox.materiales set nombre = '{nombre}', cantidad = '{cantidad}', descripcion = '{descripcion}', precio = {precio}, corte = '{corte}', origen = {origen} WHERE cod = {cod}"
    cursor.execute(DML)

    # Hacer permanente los cambios y cerrar conexion
    conexion.commit()
    conexion.close()

# Modificar producto
def updateProducto(cod, nombre, precio, categoria, materiales, cantidad, imagen):
     # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    if (imagen):
        DML = f"UPDATE proyectobox.productos set nombre = '{nombre}', precio = {precio}, imagen = '{imagen}', cantidad = '{cantidad}', categoria = '{categoria}' WHERE cod = {cod}"
    else:
        DML = f"UPDATE proyectobox.productos set nombre = '{nombre}', precio = {precio}, cantidad = '{cantidad}', categoria = '{categoria}' WHERE cod = {cod}"
    cursor.execute(DML)

    # Eliminamos las referencias del p_m
    DML = f"DELETE FROM proyectobox.p_m ppm WHERE ppm.cod_producto = {cod}"
    cursor.execute(DML)
    conexion.commit()

    # Insertamos los materiales del producto
    for material in materiales:
        DML = f"INSERT INTO proyectobox.p_m VALUES ({cod},{material})"
        cursor.execute(DML)

    # Hacer permanente los cambios y cerrar conexion
    conexion.commit()
    conexion.close()

# Ingresar material
def ingresarMaterial(nombre, descripcion, precio, corte, origen, cantidad):
     # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    DML = f"INSERT INTO proyectobox.materiales (nombre,descripcion,precio,corte,origen,cantidad,imagen) VALUES ('{nombre}', '{descripcion}', {precio}, '{corte}', {origen}, {cantidad}, '')"
    cursor.execute(DML)

    # Hacer permanente los cambios y cerrar conexion
    conexion.commit()
    conexion.close()

# Ingresar producto
def ingresarProducto(nombre, precio, categoria, materiales, cantidad, imagen):
    # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    DML = f"INSERT INTO proyectobox.productos (nombre,precio,categoria,cantidad,imagen) VALUES ('{nombre}', {precio}, '{categoria}', {cantidad}, '{imagen}')"
    cursor.execute(DML)

    # Insertamos los materiales del producto
    DML = f"SELECT max(cod) FROM proyectobox.productos"
    cursor.execute(DML)
    cod = cursor.fetchall()[0][0]
    for material in materiales:
        DML = f"INSERT INTO proyectobox.p_m VALUES ({cod},{material})"
        cursor.execute(DML)

    # Hacer permanente los cambios y cerrar conexion
    conexion.commit()
    conexion.close()

# Consultar paises
def consultarPaises():
    # Realizar conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Crear cursor
    cursor = conexion.cursor()

    # Creamos y ejecutamos el DML
    DML = f"SELECT cod, nombre FROM proyectobox.paises ORDER BY nombre"
    cursor.execute(DML)

    lista = cursor.fetchall()

    # Hacer permanente los cambios y cerrar conexion
    conexion.close()

    return lista