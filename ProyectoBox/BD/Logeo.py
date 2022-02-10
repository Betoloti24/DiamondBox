from mysql.connector import connect

# Metodo para consultar el ultimo ingresado
def consultarusuario(usuario, clave):
    # Realizamos la conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Invocamos el cursor
    cursor = conexion.cursor()

    # Declaramos el DML
    DML = F"SELECT * FROM usuarios WHERE usuario = '{usuario}' and clave = '{clave}'"

    # Ejecutamos la consulta
    cursor.execute(DML)

    return (len(cursor.fetchall()) > 0)

# Metodo para validar que el usuario sea unico
def validarusuario(usuario):
    # Realizamos la conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Invocamos el cursor
    cursor = conexion.cursor()

    # Declaramos el DML
    DML = F"SELECT * FROM usuarios WHERE usuario = '{usuario}'"

    # Ejecutamos la consulta
    cursor.execute(DML)

    return (len(cursor.fetchall()) > 0)

# Metodo para ingresar al usuario
def ingresarusuario(usuario, clave):
    # Realizamos la conexion
    conexion = connect(host = "localhost", user = "root", password = "2357", database = "proyectobox", port = "3306")

    # Invocamos el cursor
    cursor = conexion.cursor()

    # Declaramos el DML
    DML = F"INSERT INTO proyectobox.usuarios (usuario, clave) VALUES ('{usuario}', '{clave}')"

    # Ejecutamos la consulta
    cursor.execute(DML)
    # Mantener los cambios en la BD
    conexion.commit()
