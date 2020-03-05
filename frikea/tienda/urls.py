from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('productos/', ListaProducto.as_view(), name='productos'),
    path('listcategorias/', ListaCategorias.as_view(), name='listcategorias'),
    path('producategorias/<int:pk>', CategoriaProducto.as_view(), name='producategorias'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('cart/', login_required(ListaCarrito.as_view()), name='cart'),
    path('agregar/<int:pk>', login_required(AgregarProducto.as_view()), name='agregar'),
    path('eliminar/<int:pk>', login_required(EliminarProducto.as_view()), name ='eliminar'),
    path('pagar/', login_required(VaciarCarrito.as_view()), name ='pagar'),
]
