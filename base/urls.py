
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logoutUser, name='logout'), 
    path('register/', views.registerUser, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Add more URL patterns here
]