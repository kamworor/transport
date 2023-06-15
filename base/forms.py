from django import forms
from django.forms import ModelForm
from .models import Vehicles, Messages, Display

class VehiclesForm(ModelForm):
    class Meta:
        model = Vehicles
        fields = ['numberPlate','vehicleType','vehicle_image'] 
        

class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['name','email','message']

class DisplayForm(ModelForm):
    class Meta:
        model = Display
        fields = ['vehicles'] 


