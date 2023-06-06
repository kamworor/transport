from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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
    return render(request, 'login.html', context) 

def logoutUser(request):
    logout(request)
    return render(request, 'home.html')

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
   
    return render(request, 'register.html', {'form':form})

def home(request):
    return render(request,'home.html' )

def dashboard(request):
     return render(request, 'dashboard.html')

