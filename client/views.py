from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from base.decorators import  allowed_users
from .forms import OrderForm,VehiclesForm
from .models import Vehicles,Client,Order
from base.models import Vehicles


# Create your views here.


def home(request):
    return render(request,'client/home.html' )  


@allowed_users(allowed_roles=['client'])
def dashboards(request):
    vehicles = Vehicles.objects.filter(selected=False)
    orders = Order.objects.filter(status='Available')
    try:    
      
        client = get_object_or_404(Client, user=request.user) 

          # Retrieve the selected vehicle IDs from the session
        session_key = 'selected_vehicle_ids_' + str(client.id)
        selected_vehicle_ids = request.session.get(session_key, []) 
        selected_vehicles = Vehicles.objects.filter(id__in=selected_vehicle_ids)

    except ObjectDoesNotExist: 
        client = None
        selected_vehicles = []


    context ={'vehicles':vehicles,
              'orders':orders,
              'selected_vehicles':selected_vehicles,
              'client':client} 
    return render(request, 'client/dashboards.html', context) 

  
@allowed_users(allowed_roles=['client'])    
def orders(request):
    if request.method =='POST':
       selected_vehicle_ids = request.POST.getlist('boxes') 
       print(selected_vehicle_ids)
       client = Client.objects.get(user=request.user)
       # Clear existing orders and create new ones for selected vehicles
       client.order_set.all().delete()
       
       #   # Store the selected vehicle IDs in the session
       session_key = 'selected_vehicle_ids_' + str(client.id)
       request.session[session_key] = selected_vehicle_ids
      

         # Create new orders for selected vehicles
       for vehicle_id in selected_vehicle_ids:
              vehicle = Vehicles.objects.get(id=vehicle_id)
              print(vehicle)
             
              Order.objects.create(client=client, vehicles=vehicle, status='Booked')
        
       return redirect('dashboards')
    else:
        form = OrderForm()  
    
    context = {'form':form}
    return render(request, 'client/save_vehicle.html', context)
             
             


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

