from django import forms 
from .models import *

class AgregarForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['cantidad']
        labels = {
            'cantidad': 'Cuántos vallevar?',
            
        }