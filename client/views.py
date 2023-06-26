from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import OrderForm,VehiclesForm
from .models import Vehicles,Client,Order
from base.models import Vehicles 


# Create your views here.

def home(request):
    return render(request,'client/home.html' )  

def dashboards(request):
    vehicles = Vehicles.objects.all() 
    selected_vehicles = Order.objects.all()
    print(selected_vehicles)
    
    context ={'vehicles':vehicles,'selected_vehicles':selected_vehicles}
   
    
    return render(request,'client/dashboards.html',context)
  
   
 

 
def display_vehicles(request):
    
    selected_vehicles = Order.objects.filter(vehicles__name='vehicles')
  

    context = { 'selected_vehicles':selected_vehicles}
       
    return render(request, 'client/dashboards.html',context) 


@login_required
def client(request, pk):
    user = request.User

    try:
         client = Client.objects.get(user=user)

    except Client.DoesNotExist:
        client = Client(user=user)
        client.save()

    client = Client.objects.get(id=pk)

    orders= client.order_set.all()
   
    booked =Vehicles.objects.filter(status='Booked').count
    available =Vehicles.objects.filter(status='Available').count
   

    context ={'client':client,'available':available, 'booked':booked,'orders':orders}
    return render(request,'client/client.html', context)





 