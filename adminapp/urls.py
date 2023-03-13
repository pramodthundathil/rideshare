from django.urls import path

from .import views

urlpatterns = [
    path("AdminHome",views.AdminHome,name="AdminHome"),
    path("UserView/<int:pk>",views.UserView,name="UserView"),
    path("Approvel/<int:pk>",views.Approvel,name="Approvel"),
    path("DeleteUser/<int:pk>",views.DeleteUser,name="DeleteUser"),
    path("AdminMessages",views.AdminMessages,name="AdminMessages"),
    path("AddAdminReplay/<int:pk>",views.AddAdminReplay,name="AddAdminReplay")
    
]
