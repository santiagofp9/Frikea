from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class SigninForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username']
        labels = {
            'first_name': '¿Cuál es su nombre?',
            'last_name': '¿Cuál es su apellido?',
            'username': 'Elija el nombre de sus sueños',
        }

