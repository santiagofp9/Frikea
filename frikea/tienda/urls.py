from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('productos/', ListaProducto.as_view(), name='productos'),
    path('listcategorias/', ListaCategorias.as_view(), name='listcategorias'),
    path('producategorias/<int:pk>', CategoriaProducto.as_view(), name='producategorias'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('cart/', Cart.as_view(), name='cart'),
]
