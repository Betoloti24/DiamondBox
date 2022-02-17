from os import name
from django.urls import path
from .views import inventario, agregarMaterial, agregarProducto, consultar, modificarMaterial, modificarProducto

urlpatterns = [
    path('inventario/', inventario, name="inventario"),
    path('agregarM/', agregarMaterial, name="agregarM"),
    path('agregarP/', agregarProducto, name="agregarP"),
    path('consultar/', consultar, name="consultar"),
    path('modificarM/<int:codigo>', modificarMaterial, name="modificarM"),
    path('modificarP/<int:codigo>', modificarProducto, name="modificarP"),
]