
from django.shortcuts import render, redirect
from userauths import forms as userauths_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from doctor import models as doctor_models
from patient import models as patient_models
from userauths import models as userauths_models


# Create your views here.

def home(request):
    return render(request, 'users/profile.html')


def register_view(request):
    # if request.user.is_authenticated:
    #     messages.success(request, "You are already logged in ")
    #     return redirect("/")
    
    if request.method == "POST":
        form = userauths_form.UserRegisterForm(request.POST or None )

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get("password1")
            user_type = form.cleaned_data.get("user_type")

            user =authenticate(email=email, password=password1 )
            print('user====', user)

            if user is not None:
                login(request, user)

                if user_type == "Doctor":
                    doctor_models.Doctor.objects.create(user=user,full_name = username)

                else:
                    patient_models.Patient.objects.create(user=user,full_name =username,email=email)
    

            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('/')
    else:
        form = userauths_form.UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

def Login_view(request):
    # if request.user.is_authenticated:
    #     messages.success(request, "You are already logged in ")
    #     return redirect("/")
    
    if request.method == "POST":
        form = userauths_form.LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            try:
                user_instance = userauths_models.User.objects.get(email=email, is_active=True)
                user_authenticate = authenticate(request, email = email,password = password)

                if user_authenticate is not None:
                    login(request,user_authenticate)

                    messages.success(request, "Account Created successfully")

                    next_url = request.GET.get('next','/')
                    return redirect(next_url)
                else:
                    messages.error(request,"Username or password does not exist")
            except:
                messages.error(request,"User does not exist")
    else:
        form = userauths_form.LoginForm()
        context = {
            'form':form
        } 
        return render(request,"users/login.html",context)   

def Logout_view(request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return redirect('login/')        


