from django.urls import path
from app5.views import *

urlpatterns = [
  
    path('loop/',loop,name ='loop'),
    path('condition/',condition,name='condition'),
    
]

