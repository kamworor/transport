from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logoutUser, name='logout'), 
    path('register/', views.registerUser, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('display/', views.display, name='display'), 
    path('services/', views.services, name='service'), 
    # Add more URL patterns here
]+   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)