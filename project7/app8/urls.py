from django.urls import path
from app8.views import *

urlpatterns = [
    path('gongura/',gongura,name='gongura'),
]
