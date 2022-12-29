from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Rides(models.Model):
   
    options2 = (("completed","completed"),
               ("pending","pending"),
               ("ongoing","ongoing"),
               ("cancelled","cancelled"))
    
    Rideid = models.AutoField(primary_key=True)
    RiderId = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    Ridemode = models.CharField(max_length=255)
    Departure_Place = models.CharField(max_length=255)
    Departure_time = models.DateTimeField(auto_now_add=False)
    Arrival_palce = models.CharField(max_length=255)
    Allowed_Passengers = models.CharField(max_length=255)
    Arrival_time = models.DateTimeField(auto_now_add=False)
    Price = models.CharField(max_length=255)
    Ridestatus = models.CharField(max_length=255,choices=options2)
    
class OngoingRides(models.Model):
    options = (("completed","completed"),
               ("pending","pending"),
               ("ongoing","ongoing"),
               ("cancelled","cancelled"))
    
    Ongoingid = models.AutoField(primary_key=True)
    Rideid = models.ForeignKey(Rides,on_delete=models.CASCADE)
    Passenger = models.ForeignKey(User,on_delete=models.CASCADE)
    RideStatus = models.CharField(max_length=255,choices=options)
    comments = models.CharField(max_length=1000)
    
    
    
    
    
