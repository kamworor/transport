from django.contrib import admin

# Register your models here.

from .models import Vehicles,Messages

admin.site.register(Vehicles)
admin.site.register(Messages) 
