from django.db import models
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="Nombre de usuario",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingresa el nombre de usuario',
                'class':'login__input'
            }
        )
    )

    password = forms.CharField(
        required=True,
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingresa la contraseña',
                'class':'login__input'
            }
        )
    )