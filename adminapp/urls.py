from django.urls import path

from .import views

urlpatterns = [
    path("AdminHome",views.AdminHome,name="AdminHome"),
    path("UserView/<int:pk>",views.UserView,name="UserView"),
    path("Approvel/<int:pk>",views.Approvel,name="Approvel"),
    
]
