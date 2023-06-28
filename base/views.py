from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import VehiclesForm, MessageForm, DisplayForm
from .models import Display,Vehicles
from client.models import Order,Client

def login_view(request):
    
    if request.method == 'POST': 
            username = request.POST.get('username').lower()
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login')

    context = {}
    return render(request, 'base/login.html', context)  

def logoutUser(request):
    logout(request)
    return render(request, 'base/home.html')

def registerUser(request): 
    form = UserCreationForm()

    
    if request.method == 'POST':

            form = UserCreationForm(request.POST)   
            if form.is_valid():
                user = form.save(commit=False) 
                user.username = user.username.lower()     
                user.save()
                login(request, user)
                return redirect('dashboard')
            else:
               messages.error(request, 'An error occured during registration')
   
    return render(request, 'base/register.html', {'form':form}) 

def home(request):
    return render(request,'base/home.html' ) 

def dashboard(request):
    submitted = False
    
    if request.method == 'POST':
        form = VehiclesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/base/display')
    else:
        form = VehiclesForm()
        if 'submitted' in request.GET:
            submitted = True
    
    vehicles = Vehicles.objects.all()

    clients = Client.objects.all()

    orders = Order.objects.all() 
   
    context = {
        'form': form,
        'submitted': submitted, 
        'vehicles': vehicles,
         'selected_orders': orders,
         'clients':clients
    }
    return render(request, 'base/dashboard.html', context)  
def display(request):
     display = Vehicles.objects.all()

     booked =Vehicles.filter(status='Booked').count
     available =Vehicles.filter(status='Available').count

     context = {'display':display,'booked':booked, ' available':available}
 
     return render(request, 'base/display.html',context)

def services(request):
     return render(request, 'base/service.html') 

def about(request):
     return render(request, 'base/about.html') 
 
def contact(request):
     form = MessageForm()
     if request.method == 'POST': 
          form = MessageForm(request.POST) 
          if form.is_valid():
               form = form.save() 
          return redirect('base/home')
          
     return render(request, 'base/contact.html', {'form':form}) 


