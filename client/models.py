from django.contrib.auth.models import User
from django.db import models
from base.models import Vehicles, User

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS = (
        ('Booked','Booked'),
        ('Available','Available'),
    )

    client =models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    vehicles =models.ForeignKey(Vehicles, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self): 
        return str(self.client) 

    

