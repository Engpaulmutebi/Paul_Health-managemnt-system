from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'email'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'email'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'email'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'email'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'password'}))

    class Meta:
        model = User
        fields = ['email', 'password']

