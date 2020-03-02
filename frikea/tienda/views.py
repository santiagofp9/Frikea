from django.shortcuts import render,redirect
from django.views.generic import ListView, TemplateView, CreateView
from django.urls import reverse_lazy
from .models import *

# Create your views here.

class Inicio(ListView):
    model = Producto
    template_name = 'tienda/index.html'
    context_object_name = 'produ'
    queryset = Producto.objects.all()

class About(TemplateView):
    template_name = 'tienda/about.html'

class ListaProducto(ListView):
    model = Producto
    template_name = 'tienda/product.html'
    context_object_name = 'produ'
    queryset = Producto.objects.all()
