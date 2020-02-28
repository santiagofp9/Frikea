from django.shortcuts import render,redirect
from django.views.generic import ListView, TemplateView, CreateView
from django.urls import reverse_lazy
"""from .forms import EstuForm"""
from .models import *

# Create your views here.

class Inicio(TemplateView):
    template_name = 'tienda/index.html'

class About(TemplateView):
    template_name = 'tienda/about.html'

class ListaProducto(ListView):
    model = Producto
    template_name = 'tienda/product.html'
    context_object_name = 'produ'
    queryset = Producto.objects.all()

