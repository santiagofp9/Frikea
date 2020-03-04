from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from usuario.forms import FormularioLogin, SigninForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView


# Create your views here.

class RegistroUsu(CreateView):
    model = User
    template_name = 'tienda/registroUsu.html'
    form_class = SigninForm
    success_url = reverse_lazy('tienda:inicio')

class LoginUsu(FormView):
    model = User
    template_name = 'tienda/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('tienda:inicio')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else: 
            return super(LoginUsu, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginUsu, self).form_valid(form)

def LogoutUsu(request):
    logout(request)
    return HttpResponseRedirect('/')




