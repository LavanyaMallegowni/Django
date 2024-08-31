from django.urls import path
from app6.views import *

urlpatterns = [
    path('flowers/',flowers,name ='flowers'),
    path('loop/',loop,name ='loop')
]

