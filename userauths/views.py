
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from userauths import forms as userauths_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in ")
        return redirect("/")
    
    if request.method == "POST":
        form = userauths_form.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

