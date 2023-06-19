from django import forms
from django.forms import ModelForm
from .models import Vehicles, Messages, Display

class VehiclesForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = ['numberPlate', 'vehicleType', 'vehicle_image']
        widgets = {
            'numberPlate': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicleType': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'numberPlate': 'Number Plate',
            'vehicleType': 'Vehicle Type',
            'vehicle_image': 'Vehicle Image',
        }

class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['name','email','message']
        

class DisplayForm(ModelForm):
    class Meta:
        model = Display
        fields = ['vehicles'] 
