from pathlib import Path
from unittest.mock import patch
from django.urls import path
from .import views

urlpatterns = [
    path("rides/<int:val>",views.rides,name="rides"),
    path("AddRide",views.AddRide,name="AddRide"),
    path("ReserveDrive/<int:pk>",views.ReserveDrive,name="ReserveDrive"),
    path('FinishTrip/<int:pk>',views.FinishTrip,name="FinishTrip"),
    path("Myrides",views.Myrides,name="Myrides"),
]
