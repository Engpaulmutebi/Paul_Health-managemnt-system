from django.shortcuts import render
from Base import models as base_models


def home(request):
    services = base_models.Service.objects.all()

    context = {
        'services':services
    }
    
    return render(request, 'users/profile.html',context)
