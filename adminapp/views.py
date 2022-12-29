from django.shortcuts import render,redirect
from Home.models import UserDetails
from django.contrib.auth.models import User
from django.contrib import messages

from ride.models import Rides
# Create your views here.

def AdminHome(request):
    unapprovedusers = UserDetails.objects.all()
    users = User.objects.all()
    ap_users = User.objects.filter(is_active = False) 
    rides = Rides.objects.all()
    
    
    context = {
        'unapprovedusers':unapprovedusers,
        "users":users,
        "userlegth":len(users),
        "ap_userlegth": len(ap_users),
        "rides":rides
    }
    
    return render(request,"adminindex.html",context)

def UserView(request,pk):
    userdetail = UserDetails.objects.filter(DetailID = pk)
    context = {
        "userdetail":userdetail
    }
    return render(request,'userview.html',context)

def Approvel(request,pk):
    userdetails = UserDetails.objects.get(DetailID = pk)
    id = userdetails.UserID.id
    user = User.objects.get(id = id)
    
    if user.is_active == True:
        user.is_active = False
        user.save()
        messages.info(request,"User DeActivated")
        
    else:
        user.is_active = True
        user.save()
        messages.info(request,"User Activated")
        
    return redirect("UserView", pk = pk)
    
    
    
    