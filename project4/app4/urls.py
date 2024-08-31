from django.urls import path
from app4.views import *

urlpatterns = [
    path('rose/',rose,name='rose'),
]
