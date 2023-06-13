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
<<<<<<< HEAD
    path('services/', views.services, name='service'), 
=======
    path('service/', views.services, name='service'), 
    path('contact/', views.contact, name='contact'), 
   
>>>>>>> d4b8874df03d6378952aa441cf5de5a541c3f0d6
    # Add more URL patterns here
]+   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)