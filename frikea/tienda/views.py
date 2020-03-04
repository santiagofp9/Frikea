from django.shortcuts import render,redirect
from django.views.generic import ListView, TemplateView, CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.


    
class Inicio(ListView):
    model = Producto
    template_name = 'tienda/index.html'
    context_object_name = 'produ'
    queryset = Producto.objects.all()

class About(TemplateView):
    template_name = 'tienda/about.html'
    
class Contact(TemplateView):
    template_name = 'tienda/contact.html'


class ListaProducto(ListView):
    model = Producto
    template_name = 'tienda/product.html'
    context_object_name = 'produ'
    queryset = Producto.objects.all()


class ListaCategorias(ListView):
    model = Categoria
    template_name = 'tienda/categories.html'
    context_object_name = 'catego'
    queryset = Categoria.objects.all()


class CategoriaProducto(ListView):
    model = Producto
    template_name = 'tienda/productCatego.html'

    def get_context_data(self, **kwargs):
       	context = super(CategoriaProducto, self).get_context_data(**kwargs)
       	parametro = self.kwargs.get('pk', None)
       	context['produ'] = Producto.objects.filter(categoria=parametro)
        context['catenom'] = Categoria.objects.filter(id=parametro)
        print(context['catenom'])
        print(context['produ'])
       	return context

class Cart(TemplateView):
    template_name = 'tienda/carrito.html'

class AgregarProducto(CreateView):
    model = Carrito
    template_name = 'agregarProducto.html'
    form_class = AgregarForm
    success_url = '/' 
