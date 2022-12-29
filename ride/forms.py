from django.forms import ModelForm
from .models import Rides

class RideAddForm(ModelForm):
    
    class Meta:
        model = Rides
        fields = "__all__"
