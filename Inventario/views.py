from django.shortcuts import render
from ProyectoBox.Metodos.Productos import listaProductos, listaMateriales

# Vista del inventario
def inventario(request):
    # Verificamos si se posee algun metodo del request
    if (request.method == "POST"):
        print(request.POST)

    # Declaramos el contexto
    contexto = {
        "productos": listaProductos(),
        "materiales": listaMateriales()
    }

    # Renderizar pagina    
    return render(request, 'inventario.html', contexto)

# Vista de Agregar Material
def agregarMaterial(request):
    pass

# Vista de Agregar Producto
def agregarProducto(request):
    pass

# Vista de Consultar
def consultar(request):
    pass

# Vista de Modificar Material
def agregarMaterial(request):
    pass