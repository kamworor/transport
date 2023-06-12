from django import forms
from django.forms import ModelForm
from .models import Vehicles

class VehiclesForm(ModelForm):
    class Meta:
        model = Vehicles
        fields = ['numberPlate','vehicleType','vehicle_image'] 