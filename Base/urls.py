
from django.urls import path
from . import views

app

urlpatterns = [
    path('', views.home, name='home'),
    path('service/<service_id>/', views.service_detail, name='service'),
]
