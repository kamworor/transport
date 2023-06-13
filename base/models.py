from django.contrib.auth.models import User
from django.db import models



# Create your models here.

class Vehicles(models.Model):
    numberPlate = models.CharField(max_length=200)
    vehicleType = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    vehicle_image = models.ImageField(null=True, blank=True, upload_to="images/")
    status = models.BooleanField(default=False) 

    def __str__(self):
        return str(self.numberPlate)
    
class Display(models.Model):
    vehicles = models.ForeignKey(Vehicles, on_delete=models.CASCADE) 

 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True,upload_to="images/")

    def __str__(self):
        return self.user.username
    
class Messages(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name
