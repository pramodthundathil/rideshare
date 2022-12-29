from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .forms import UserAddform,UserDetailForm
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from ride.models import Rides, OngoingRides

from .decorators import admin_only


# Create your views here.
@admin_only
def home(request):
    
    ongoingrides = OngoingRides.objects.filter(Passenger = request.user)
    context = {
        "ongoingrides":ongoingrides
    }
    return render(request,"index.html",context)

def admin_page(request):
    return render(request,"adminindex.html")


def signin(request):
    
    if request.method  == 'POST':
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('home')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('signin')
    
    return render(request,'login.html')
    
   

def signup(request):
    
    userform = UserAddform()
    
    if request.method == 'POST':
        
        form = UserAddform(request.POST)
        
        if form.is_valid():
            
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')
            
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('registration')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('registration')
            
            else:
                new_user = form.save()
                new_user.is_active = False
                new_user.save()
                pk = new_user.id
                
                group = Group.objects.get(name="user")
                new_user.groups.add(group)
                
                
                messages.success(request,"Your Account Created Successfully Fill out the Feilds To Activate User Account")
                return redirect('UserDetails', pk = pk)
    
    return render(request,"register.html",{"userform":userform})

def UserDetails(request,pk):
    userdetailform = UserDetailForm()
    user = User.objects.get(id = pk)
    
    if request.method == "POST":
        userdetailform = UserDetailForm(request.POST,request.FILES)
        if userdetailform.is_valid():
            userdetail = userdetailform.save()
            userdetail.UserID = user
            userdetail.save()
            return redirect("home")
        else:
            return HttpResponse("Form is Not Valid")
    
    context = {
        "userdetailform":userdetailform,
    }
    return render(request,"authdetails.html",context)

def signout(request):
    
    logout(request)
    return redirect('home')
