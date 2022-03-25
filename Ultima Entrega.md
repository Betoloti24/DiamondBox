# SD Accesorios

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Aplicacion web para el control de inventario de una empresa de venta de joyas, piedras preciosas y material para hacer accesorios. Posee 2 módulos, un módulo de *Usuarios*, que comprende el **Inicio de Sesion**, el **Registro de Usuarios** y el **Cierre de Sesión**, y otro módulo de *Inventario*, que posee las funciones de **Modificar**, **Crear**, **Eliminar** y **Consultar** productos y materiales.

## Módulo de Usuario

### Inicio de Sesión (Logeo)

<center>

#### FLUJO IDEAL

</center>

Posee una interfaz amigable para el inicio de sesión, donde; si ya está registrado, con simplemente ingresar el usuario y la contraseña puede acceder a la aplicación.

<p align="center"> 
<img src="https://imgur.com/0QP8gAK.png"> 
</p>

Consultando la base de datos podemos ver los usuarios que estan registrados.

<p align="center"> 
<img src="https://imgur.com/NW85WGl.png"> 
</p>

Ingresando uno de los usuarios de la base de datos, podemos ver que ingresamos a la aplicacion de forma satisfactoria.

<p align="center"> 
<img src="https://imgur.com/OdaSFwj.png"> 
<img src="https://imgur.com/ICbnwmI.png"> 
</p>

<center>

#### FLUJOS ALTERNOS

</center>

1. **Datos Faltantes**

Sí se deja en blanco cualquiera de los campos del formulario, la aplicación nos resalta que el campo es requerido.

<p align="center"> 
<img src="https://imgur.com/vWl1z7c.png"> 
</p>

2. **Error de usuario o contraseña**

Sí se colocan credenciales que no estan registradas en la base de datos, esto arroja un error donde le solicita al usuario que vuelva a intentar, ya que la clave o contraseña no son correctos.

<p align="center"> 
<img src="https://imgur.com/xUBoLDj.png"> 
<img src="https://imgur.com/QZGKICP.png"> 
</p>

### Registro de Usuarios

<center>

#### FLUJO IDEAL

</center>

Accedemos a el desde la pagina de *Inicio de Sesión* pulsando el botón de *Registrarse*.

<p align="center"> 
<img src="https://imgur.com/RV8q5ad.png"> 
</p>

Lo que nos mostrará una interfaz cómoda que solicita los datos para un nuevo usuario y una clave de seguridad que debe de conocer el administrador de la aplicación, dicha clave de seguridad es *2357*; sin embargo, puede cambiarse a nivel de código. Al ingresar todos los datos completos, accede a la pagina del inventario y se registra el usuario en la base de datos.

<p align="center"> 
<img src="https://imgur.com/HwikUuq.png"> 
<img src="https://imgur.com/jvMEYAa.png"> 
<img src="https://imgur.com/ICbnwmI.png"> 
<img src="https://imgur.com/pH4gTAj.png"> 
</p>

<center>

#### FLUJOS ALTERNOS

</center>

1. **Campos en blanco**

Se cumplen las mismas condiciones del logeo.

<p align="center"> 
<img src="https://imgur.com/AgSJzS7.png"> 
</p>

2. **Usuario ya existente**

El nombre de usuario es el identificador del usuario, debe de ser único en la base de datos para poder diferenciarlo de los demás; por tanto, este debe de ser único, a si que si se ingresa un usuario que ya existe en la base de datos, la aplicación muestra un mensaje de error al usuario, solicitando que coloque otro usuario ya que este está ya registrado.

<p align="center"> 
<img src="https://imgur.com/BeyId96.png"> 
<img src="https://imgur.com/GtsLqxi.png"> 
</p>

3. **Clave de seguriddad errónea**

Si se coloca una clave de seguridad erronea, la aplicación muestra un mensaje al usuario para que contacte con el administrador y vuelva a ingresar la clave.

<p align="center"> 
<img src="https://imgur.com/EWoknuK.png"> 
<img src="https://imgur.com/axTRoEi.png"> 
</p>

### Cerrar Sesión

Para cerrar la sesión en la aplicación, se debe de pulsar el botón de *Cerrar Sesión* en el menú lateral izquierdo.

<p align="center"> 
<img src="https://imgur.com/IcFpdHw.png"> 
<img src="https://imgur.com/0QP8gAK.png"> 
</p>

## Módulo de Inventario

### Inventario

El inventario muestra una lista de todos los productos y materiales que se poseen, estos a su vez muestran los datos más importantes de cada producto. 
* Para el caso de los productos: Identificación, Precio, Categoría, Nombre y Cantidad.
* Para el cado de los materiales: Identificacion, Nombre, Precio, Corte (sí lo tiene), Origen y la Cantidad.

<p align="center"> 
<img src="https://imgur.com/ICbnwmI.png"> 
<img src="https://imgur.com/nn7SkD8.png"> 
<img src="https://imgur.com/o8wFmhC.png"> 
</p>

### Eliminar Producto o Material

<center>

#### FLUJO IDEAL

</center>

Ambos objetos se eliminan de la misma manera, desde el inventario, pulsando el botón rojo de *Eliminar*. Este solicitará la confirmación de la operación. 

Podemos visualizar en la base de datos como se encuentran los productos a eliminar:

<p align="center"> 
<img src="https://imgur.com/WzezDY9.png"> 
<img src="https://imgur.com/UXdtSqL.png"> 
</p>

Por consiguiente, pulsamos los botones de eliminar de cada uno de los objetos:

<p align="center"> 
<img src="https://imgur.com/EWTOVUM.png"> 
<img src="https://imgur.com/P5cLpv2.png"> 
</p>

Podemos ver que la aplicación nos muestra un mensaje de confirmación al eliminar cualquiera de los objetos.

<p align="center"> 
<img src="https://imgur.com/lbkUyJM.png"> 
<img src="https://imgur.com/TRmxE4s.png"> 
</p>

Y al revisar en la base de datos, no se consiguen los objetos elimniados.

<p align="center"> 
<img src="https://imgur.com/ZyvLJp1.png"> 
<img src="https://imgur.com/cp1KhUR.png"> 
</p>

<center>

#### FLUJOS ALTERNOS

</center>

1. **Se intenta eliminar un material que compone un producto**

Los materiales no pueden eliminarse sí estos son parte de la composición de algun producto, ya que al momento de consultar los detalles de un producto, esta información sería comprometida.

Intentamos eliminar el material *Amatista*, y vemos que nos arroja un error ya que hay al menos un producto compuesto por el.

<p align="center"> 
<img src="https://imgur.com/O3vY7ji.png"> 
<img src="https://imgur.com/oeip6hL.png"> 
</p>

2. **Cancelar operación**

Al pulsar el boton de *Elimniar*, la ventana emergente muestra una opción de cancelar, lo que cancela la operación y no elimina el producto o material.

<p align="center"> 
<img src="https://imgur.com/6LteTd3.png"> 
<img src="https://imgur.com/ICbnwmI.png"> 
</p>

### Consultar Producto o Material

<center>

#### FLUJO IDEAL

</center>

Para ambos objetos la consulta se realiza de la misma manera, pulsando el botón de *Consultar* que se encuentra en el menu de opciones lateral izquierdo.

<p align="center"> 
<img src="https://imgur.com/CBFdgzP.png"> 
</p>

Se muestra una interfaz que solicita el codigo del objeto y el tipo, que puede ser un *Producto* o un *Material*, lo que al ingresar los datos y pulsar el botón de *Buscar*, se muestran todos los datos del producto o material consultado que también están registrados en la base de datos.

<p align="center"> 
<img src="https://imgur.com/lL6b18J.png"> 
<img src="https://imgur.com/pZ8r1g6.png"> 
<img src="https://imgur.com/6m4mMR1.png"> 
<img src="https://imgur.com/AHLwz7d.png"> 
<img src="https://imgur.com/d5rmsJg.png"> 
<img src="https://imgur.com/uVIPKPC.png"> 
<img src="https://imgur.com/SoN4oNl.png"> 
<img src="https://imgur.com/kjG8v7Q.png"> 
<img src="https://imgur.com/lxVg230.png"> 
</p>

<center>

#### FLUJOS ALTERNOS

</center>

1. **Datos vacios**

Aplica lo mismo implementado en el logeo. 

<p align="center"> 
<img src="https://imgur.com/cHdzJKV.png"> 
</p>

2. **Código del objeto**

Si se ingresa un código que no está registrado en la base de datos, la aplicación muestra un mensaje al usuario para que ingrese un nuevo código, ya que el ingresado no se encuentra registrado.

<p align="center"> 
<img src="https://imgur.com/ZyvLJp1.png"> 
<img src="https://imgur.com/TQY50cB.png"> 
<img src="https://imgur.com/38IVJlp.png"> 
</p>

3. **No colocar un número entero de máximo 3 dígitos**

El código debe de ser un número entero de máximo 3 dígitos, de no ser así, la aplicación le muestra al usuario un mensaje para que vuelva a ingresar el código.

<p align="center"> 
<img src="https://imgur.com/gjkFuOx.png"> 
<img src="https://imgur.com/0aF3484.png"> 
</p>

### Ingresar un Nuevo Producto

<center>

#### FLUJO IDEAL

</center>

Para ingresar a este opción, se debe de pulsar el botón de *Agregar Producto* en el menú lateral izquierdo.

<p align="center"> 
<img src="https://imgur.com/YeVEGdG.png"> 
</p>

Lo que nos llevará a una interfaz que solicitará los datos del producto a ingresar, con lo que al llenar todos estos datos, se debe de pulsar el botón de *Agregar* y pulsar la opción de *Confirmar* de la ventana emergente.

<p align="center"> 
<img src="https://imgur.com/6d4m8yi.png"> 
<img src="https://imgur.com/mnKzovE.png"> 
<img src="https://imgur.com/HJX12EI.png"> 
<img src="https://imgur.com/BBGCOaC.png"> 
</p>

Con lo que nos llevará al inventario y nos mostrará el producto nuevo en la lista con un mensaje de confirmacion de la operación y el registro en la base de datos.

<p align="center"> 
<img src="https://imgur.com/ds6ujIn.png"> 
<img src="https://imgur.com/R5xUt7O.png"> 
<img src="https://imgur.com/0x5fKwK.png"> 
</p>

<center>

#### FLUJOS ALTERNOS

</center>

1. **Datos Vacios**

Se deben de completar todos los campos que poseen en '*' rojo, y se aplica la misma solición que en el logeo, con la diferencia que si no se selecicona una categoría o al menos un material, aparece un mensaje al usuario despues de confirmar la insersión.

<p align="center"> 
<img src="https://imgur.com/gjvfkZM.png"> 
<img src="https://imgur.com/mOAx7kD.png"> 
<img src="https://imgur.com/L2iPe2V.png"> 
</p>

2. **Cancelar Operación**

Al pulsar el botón de *Agregar*, se puede cancelar la operación pulsando el botón de *Cancelar* en la ventana emergente.

<p align="center"> 
<img src="https://imgur.com/sBAk3xS.png">
<img src="https://imgur.com/vNXPIDK.png">
</p>

### Ingresar un Nuevo Material

<center>

#### FLUJO IDEAL

</center>

Para ingresar a este opción, se debe de pulsar el botón de *Agregar Material* en el menú lateral izquierdo.

<p align="center"> 
<img src="https://imgur.com/a9zwSv2.png"> 
</p>

Lo que nos llevará a una interfaz que nos solicitará toda la informacion de un material, con lo que ingresamos los datos solicitados, pulsamos el botón de *Agregar* y confirmamos la operación.

<p align="center"> 
<img src="https://imgur.com/B64ehPv.png"> 
<img src="https://imgur.com/0CvQRpY.png"> 
<img src="https://imgur.com/TC54ypt.png"> 
<img src="https://imgur.com/bjZzg10.png"> 
</p>

Luego de esto, nos llevará al inventario con un mensaje de confirmación de la operación y con el registro en la base de datos

<p align="center"> 
<img src="https://imgur.com/DAgDz8Q.png"> 
<img src="https://imgur.com/RDWSdX4.png"> 
<img src="https://imgur.com/OC0t8gv.png"> 
</p>

<center>

#### FLUJOS ALTERNOS

</center>

1. **Datos Vacios**

Se deben de completar todos los campos que poseen en '*' rojo, y se aplica la misma solición que en el logeo, con la diferencia que si no se selecicona un *Origen*, aparece un mensaje al usuario despues de confirmar la insersión.

<p align="center"> 
<img src="https://imgur.com/oUykSqe.png"> 
<img src="https://imgur.com/IlEEVLp.png"> 
<img src="https://imgur.com/VY5yjMz.png"> 
<img src="https://imgur.com/3Fz6PeM.png"> 
</p>

2. **Cancelar Operación**

Al pulsar el botón de *Agregar*, se puede cancelar la operación pulsando el botón de *Cancelar* en la ventana emergente.

<p align="center"> 
<img src="https://imgur.com/IlEEVLp.png">
<img src="https://imgur.com/zNyrGg7.png">
<img src="https://imgur.com/IlEEVLp.png">
</p>

### Modificar Producto o Material

<center>

#### FLUJO IDEAL

</center>

Se puede acceder a esta opción al pulsar el botón de modificar en cualquier producto o material en el inventario.

<p align="center"> 
<img src="https://imgur.com/ar5XME3.png">
<img src="https://imgur.com/hODFmDm.png">
<img src="https://imgur.com/QYOwODO.png">
<img src="https://imgur.com/AtgGKNm.png">
<img src="https://imgur.com/AOs3nS1.png">
<img src="https://imgur.com/hE3uvDb.png">
</p>

Modificaremos un dato como el precio de los productos, y pulsamos el botón *Actualizar* seguida de la confirmación.

<p align="center"> 
<img src="https://imgur.com/u6bBnmo.png">
<img src="https://imgur.com/CvD0lQh.png">
<img src="https://imgur.com/7bjolOt.png">
<img src="https://imgur.com/zjMFgB5.png">
</p>

Con lo que nos enviará nuevamente al inventario, con un mensaje de confirmación y los datos modificados en la base de datos

<p align="center"> 
<img src="https://imgur.com/Zz0NKYC.png">
<img src="https://imgur.com/eAcYyhT.png">
<img src="https://imgur.com/nmqwhxR.png">
<img src="https://imgur.com/gQiv9xC.png">
<img src="https://imgur.com/Px2yRs0.png">
</p>

<center>

#### FLUJOS ALTERNOS

</center>

Todos los flujos alternos de este módulo son los mismos que se presentan en el módulo de *Creción de Productos y Materiales*


