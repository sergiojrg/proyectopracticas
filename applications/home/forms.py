from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib import messages

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

    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        print ('*******',username)
        print ('*******',password)

        if not authenticate(username=username,password=password):
            # print('mal')
            raise forms.ValidationError('Nombre de usuario o contraseña incorrectos.')
        
        return self.cleaned_data