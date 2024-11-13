from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from userauths.models import User

USER_TYPE = [
    ('Doctor','Doctor'),
    ('Patient','Patient')
]

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'email'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'ConfirmPassword'}))
    user_type = forms.ChoiceField(choices=USER_TYPE, widget=forms.Select(attrs={'class': 'form-control','placeholder':'user_type'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','user_type']

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'password'}))

    class Meta:
        model = User
        fields = ['email', 'password']

