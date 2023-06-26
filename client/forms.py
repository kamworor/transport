from django.forms import ModelForm
from .models import Order,Client,Vehicles

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields ='__all__'

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class VehiclesForm(ModelForm):
    class Meta:
        model = Vehicles
        fields = '__all__'

