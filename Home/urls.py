from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name="home"),
    path('signin',views.signin,name='signin'),
    path("signup",views.signup,name="signup"),
    path("signout",views.signout,name="signout"),
    
    path('admin_page',views.admin_page,name="admin_page"),
    path("UserDetails/<int:pk>",views.UserDetails,name="UserDetails")
    
    
]
