from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Rides,OngoingRides
# Create your views here.

@login_required(login_url="signin")
def rides(request,val):
    rides = Rides.objects.all()
    context ={
        "rides":rides
    }
    if val == 1:
        return render(request,"rides/bikerides.html",context)
    elif val == 2:
        return render(request,"rides/carrides.html",context)
    else:
        return render(request,"rides/rides.html",context)
        
        
@login_required(login_url="signin")
def AddRide(request):
    if request.method == "POST":
        
        ridemode = request.POST["ridemode"]
        departure_place = request.POST["dplace"]
        arrival_place = request.POST["aplace"]
        allowedpassengers = request.POST["allowedpass"]
        departuredate = request.POST["Ddate"]
        arrival_date = request.POST["Adate"]
        ride_price = request.POST["price"]
        
        ride = Rides.objects.create(RiderId=request.user,Ridemode=ridemode,Departure_Place=departure_place,Departure_time=departuredate,Arrival_palce=arrival_place,Allowed_Passengers=allowedpassengers,Arrival_time=arrival_date,Price=ride_price,Ridestatus="pending")
        ride.save()
        messages.info(request,"Ride Added")
        return redirect("home")
        
    return render(request,"rides/addride.html")


@login_required(login_url="signin")
def ReserveDrive(request,pk):
    ride = Rides.objects.filter(Rideid = pk)
    rideget = Rides.objects.get(Rideid = pk)
    
    if request.method == "POST":
        msg = request.POST["message"]
        ridebook = OngoingRides.objects.create(Rideid = rideget ,Passenger = request.user,RideStatus = "ongoing" ,comments = msg )
        ridebook.save()
        
        rideget.Ridestatus = "ongoing"
        rideget.save()
        
        messages.info(request,"Your Ride is Booked")
        return redirect("home") 
    
    context = {
        "ride":ride
    }
    return render(request,'rides/ridebooking.html',context)

@login_required(login_url="signin")
def FinishTrip(request,pk):
    
    if request.method == "POST":
        trip = OngoingRides.objects.get(Ongoingid = pk)
        trip.RideStatus = "completed"
        Rideid = trip.Rideid.Rideid
        trip.save()
        ride = Rides.objects.get(Rideid = Rideid )
        ride.Ridestatus = "completed"
        ride.save()
        
        messages.info(request,"Ride Completed")
        return redirect('home')
    
def Myrides(request):
    trip = OngoingRides.objects.filter(Passenger = request.user)
    context = {
        "trip":trip
    }
    
    return render(request,"rides/myrides.html",context)
        
def AddedRides(request):
    trip = Rides.objects.filter(RiderId = request.user)
    
    context = {
        "trip":trip
    }
    
    return render(request,'rides/hostedrides.html',context)
