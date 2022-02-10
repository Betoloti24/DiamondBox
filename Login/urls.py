from os import name
from django.urls import path
from .views import logeo, registro

urlpatterns = [
    path('', logeo, name='logeo'),
    path('registro/', registro, name="registro"),
]