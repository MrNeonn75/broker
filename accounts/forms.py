from django.forms import CharField, EmailField, PasswordInput, TextInput, EmailInput, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.forms import PasswordResetForm
from django import forms
from .models import Accounts


class RegisterForm(UserCreationForm):
    
    first_name = CharField(label='Ad', widget=TextInput(attrs={
        'placeholder' : 'Ad',
        'class'       : 'form-control',
        'type'        : 'text',
        'id'          : 'last_name',
    }))
    last_name = CharField(label='Soyad', widget=TextInput(attrs={
        'placeholder' : 'Soyad',
        'class'       : 'form-control',
        'type'        : 'text',
        'id'          : 'last_name'
    }))
    username = CharField(label='İstifadəçi adı', widget=TextInput(attrs={
        'placeholder' : 'İstifadəçi adı',
        'class'      : 'form-control', 
        'type'       : 'text',
        'id'         : 'username',
    }))
    email = EmailField(label='Email', widget=EmailInput(attrs={
        'placeholder' : 'Email',
        'class'       : 'form-control',
        'type'        : 'email',
        'id'          : 'email',
    }))
    password1 = CharField(label='Şifrə', widget=PasswordInput(attrs={
        'placeholder' : 'Şifrə',
        'class'       : 'form-control',
        'type'        : 'password',
        'id'          : 'password1',
    }))
    password2 = CharField(label='Şifrə təkrar', widget=PasswordInput(attrs={
        'placeholder' : 'Şifrə təkrar',
        'class'       : 'form-control',
        'type'        : 'password',
        'id'          : 'password2',
    }))

    class Meta:
        model = Accounts  
        fields = ('first_name','last_name','email' ,'username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = UsernameField(label='İstifadəçi adı', widget=EmailInput(attrs={
        'placeholder' : 'İstifadəçi adı',
        'class'       : 'form-control',
        'type'        : 'text',
        'id'          : 'email',
    }))

    password = CharField(label='Şifrə', widget=PasswordInput(attrs={
        'placeholder' : 'Şifrə',
        'class'       : 'form-control',
        'type'        : 'password',
        'id'          : 'password',
    }))

    def clean(self):
        password = self.cleaned_data.get("password")

        if not password[0].isupper():
            raise forms.ValidationError({''})

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))