from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
]