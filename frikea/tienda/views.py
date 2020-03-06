from django.shortcuts import render,redirect
from django.views.generic import View, ListView, TemplateView, CreateView, DeleteView
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

class Single(TemplateView):
    template_name = 'tienda/single.html'
    
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
       	return context

class AgregarProducto(CreateView):
    model = Carrito
    template_name = 'tienda/agregarProducto.html'
    form_class = AgregarForm
    success_url = reverse_lazy('tienda:inicio')

    def get_context_data(self, **kwargs):
        context=super(AgregarProducto, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('pk', None)
        context['producto'] =Producto.objects.filter(id=parametro)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        producto = Producto.objects.get(pk = self.kwargs.get('pk', None))
        self.object.producto = producto
        user = self.request.user.id
        usuario = User.objects.get(pk = user)
        self.object.usuario = usuario
        self.object.save()
        return super(AgregarProducto, self).form_valid(form)

class ListaCarrito(ListView):
    model = Carrito
    template_name = 'tienda/carrito.html'
    
    def get_context_data(self, **kwargs):
        context=super(ListaCarrito, self).get_context_data(**kwargs)
        user = self.request.user.id
        usuario = User.objects.get(pk = user)
        context['carr'] =Carrito.objects.filter(usuario=usuario)
        return context
        

class EliminarProducto(DeleteView):
    model = Producto
    success_url = reverse_lazy('tienda:cart')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class VaciarCarrito(View):
    model = Carrito

    def get(self, request, *args, **kwargs):
        user = self.request.user.id
        usuario = User.objects.get(pk = user)
        
        Carrito.objects.filter(usuario=usuario).delete()
        return redirect('tienda:cart')
        
         


