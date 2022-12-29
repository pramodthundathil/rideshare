
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from Home import urls
import Home

from ride import urls
import ride

from adminapp import urls
import adminapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(Home.urls)),
    path('ride/',include(ride.urls)),
    path("adminapp/",include(adminapp.urls)),
    
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

