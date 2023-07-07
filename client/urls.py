from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from base.models import Vehicles
from . import views



app_name = 'client'
urlpatterns = [
    path('', views.home, name="home"),
    path('dashboards/', views.dashboards, name="dashboards"),
    path('client/<str:pk>/', views.client, name="client"),
   path('save_vehicle/', views.orders, name='save_vehicle'),
    #path('client/orders/', views.orders, name="orders"),
    path('client/orders/', views.orders, name="orders"),
   

    #path('login/', views.login_view, name='login'), 
    #path('logout/', views.logoutUser, name='logout'), 
    #path('register/', views.registerUser, name='register'),
    #path('dashboard/', views.dashboard, name='dashboard'), 
    #path('display/', views.display, name='display'), 


    #path('service/', views.services, name='service'), 
    #path('contact/', views.contact, name='contact'), 
   

    # Add more URL patterns here
]+   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)