# Instalacion del Proyecto

## Aplciaciones Necesarias

1. Interprete de Python
2. MBD MySQL
3. NodeJS Instalado
4. Editor VSC

## Paquetes de Python

1. DJango 4.0 o superior
2. mysql-connector 2.2.9
3. mysql-connector-python 8.0.22
4. mysqlclient 2.1.0

## Ejecucion del Proyecto

1. Ejecute el MBD MySQL, y cree una conexion con las siguientes caracteristicas:
    * HOST: localhost
    * PORT: 3306
    * USER: root
    * PASSWORD: 2357
2. Cree una BD llamada proyectobox
3. Ejecute el archivo de CrearBD.sql ubicado en ProyectoBox\BD\Archivos en el MBD
4. Ejecute el archivo Insertar.sql en la misma ubicacion en el MBD
5. Corra el servidor del proyecto ejecutando en la terminal a raiz de la carpeta DiamonBox el comando

```bat
    python manage.py runserver
```
