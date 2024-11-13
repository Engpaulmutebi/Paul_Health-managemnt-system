from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.Login_view, name='login'),
    path('logout/', views.Logout_view, name='logout'),
]
