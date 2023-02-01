from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the name of the city',
    }))

    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the name of the city',
    }))

    class Meta:
        model = User
        fields = ('username', 'password')
