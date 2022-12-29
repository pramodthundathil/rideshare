from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    
    DetailID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Phone = models.IntegerField()
    House = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    Contry = models.CharField(max_length=255)
    PostalCode = models.CharField(max_length=255)
    Document = models.FileField(upload_to="user_documents",null=True,blank=True)
    Message = models.CharField(max_length=255,null=True,blank=True)
    
        
