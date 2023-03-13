from django.shortcuts import render,redirect
from Home.models import UserDetails,UserMessages
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
        "rides":rides,
        "usermessages":UserMessages.objects.all().count
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

def DeleteUser(request,pk):
    user = UserDetails.objects.get(DetailID = pk)
    mainuser  = user.UserID
    mainuser.delete()
    user.delete()
    return redirect("AdminHome")

def AdminMessages(request):
    unapprovedusers = UserDetails.objects.all()
    users = User.objects.all()
    ap_users = User.objects.filter(is_active = False) 
    rides = Rides.objects.all()
    mesg = UserMessages.objects.all()
    
    context = {
        'unapprovedusers':unapprovedusers,
        "users":users,
        "userlegth":len(users),
        "ap_userlegth": len(ap_users),
        "rides":rides,
        "mesg":mesg
    }
    return render(request,'adminmessagehadling.html',context)

def AddAdminReplay(request,pk):
    replay = request.POST['replay']
    msg = UserMessages.objects.get(id = pk)
    msg.AdminMessage = replay
    msg.save()
    return redirect("AdminMessages")
    
    
    
    