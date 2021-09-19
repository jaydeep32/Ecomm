from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

User = settings.AUTH_USER_MODEL


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder': 'Username', 'onfocus':"this.placeholder = ''" ,'onblur':"this.placeholder = 'Username'"}
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder': 'Password', 'onfocus':"this.placeholder = ''" ,'onblur':"this.placeholder = 'Password'"}
        ))
