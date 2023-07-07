from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from client.models import Client


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                group_names = list(request.user.groups.values_list('name', flat=True))
                
                if 'client' in group_names  and view_func.__name__ != 'dashboards': 
                 return redirect(reverse('client:dashboards'))
                else:
                 return view_func(request, *args, **kwargs)

            return view_func(request, *args, **kwargs) 
             
        return wrapper_func 
    return decorator




