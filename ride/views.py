from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Rides,OngoingRides
from datetime import datetime
# Create your views here.

import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from datetime import datetime


razorpay_client = razorpay.Client(
  auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))



@login_required(login_url="signin")
def rides(request,val):
    date =  datetime.now()
    rides = Rides.objects.filter(Arrival_time__gte = date)
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
        return redirect("Payment",pk=pk) 
    
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

def DeleteMyride(request,pk):
    trip = OngoingRides.objects.get(Ongoingid = pk)
    trip.delete()
    messages.info(request,"Ride deleted")
    return redirect("Myrides")

def Payment(request,pk):
    rideget = Rides.objects.get(Rideid = pk)
    
    currency = 'INR'
    amount = int(rideget.Price) * 100 # Rs. 200
    

  # Create a Razorpay Order Pyament Integration.....
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                          currency=currency,
                          payment_capture='0'))

  # order id of newly created order.
    razorpay_order_id = razorpay_order["id"]
    callback_url = 'paymenthandler/'

  # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url 
    context['slotid'] = rideget.Rideid
    context["amount"] = rideget.Price
        
    rideget = Rides.objects.get(Rideid = pk)
    return render(request,"Payment.html",context)
    
    
@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

      # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                amount = 800 * 100 # Rs. 200
                try:
                    print("working 1")
                    razorpay_client.payment.capture(payment_id, amount)
                    return redirect('Bookingconfirm')
          # render success page on successful caputre of payment
                except:
                    print("working 2")
                    return redirect('Bookingconfirm')
                    
                    
          # if there is an error while capturing payment.
            else:
                return render(request, 'paymentfail.html')
        # if signature verification fails.    
        except:
            return HttpResponseBadRequest()
        
      # if we don't find the required parameters in POST data
    else:
  # if other than POST request is made.
        return HttpResponseBadRequest()
    
def Bookingconfirm(request):
    return render(request,"confirmbooking.html")
        
        
