from django.forms import forms,Textarea,TextInput,PasswordInput,ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserDetails



class UserAddform(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control','placeholder':'User Name'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            "password2" : PasswordInput(attrs={'class': 'form-control'}),

        }
        
class UserDetailForm(ModelForm):
    
    class Meta:
        model = UserDetails
        fields = ("Phone","House","Location","State","Contry","PostalCode","Document","Message")
        widgets = {
            "Phone":TextInput(attrs={'class': 'form-control','pattern':"[0-9]{10,12}", 'title':"Please enter the mobile number with specific country code(uae : 00971xxxxxxxxx, India : 0091xxxxxxxxxx, etc..)"}),
            "House":TextInput(attrs={'class': 'form-control'}),
            "Location":TextInput(attrs={'class': 'form-control'}),
            "State":TextInput(attrs={'class': 'form-control'}),
            "Contry":TextInput(attrs={'class': 'form-control'}),
            "PostalCode":TextInput(attrs={'class': 'form-control'}),
            "Message":TextInput(attrs={'class': 'form-control'})
            }

        
        


