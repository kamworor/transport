from django.contrib import admin

# Register your models here.

from .models import Vehicles,Messages, Display

admin.site.register(Vehicles)
admin.site.register(Messages) 
admin.site.register(Display) 
