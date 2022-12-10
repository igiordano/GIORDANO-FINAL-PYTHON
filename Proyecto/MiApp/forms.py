from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CrearCursoForm(forms.Form):

    nombre = forms.CharField(min_length=5,max_length=40)
    comision = forms.IntegerField()

class CrearinstructorForm(forms.Form):
    nombre= forms.CharField(min_length=5,max_length=40)
    apellido= forms.CharField(min_length=5,max_length=40)
    email= forms.EmailField()
    profesion= forms.CharField(min_length=5,max_length=30)

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class UserEditForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k: '' for k in fields}
