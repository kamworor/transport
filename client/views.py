from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from .forms import VehiclesForm, MessageForm, DisplayForm
#from .models import Display,Vehicles,UserProfile,Messages 

# Create your views here.

def home(request):
    return render(request,'client/home.html' ) 

def client(request):
    return render(request,'client/anything.html')

def clientdash(request):
    return render(request,'client/dashboardc.html')

 