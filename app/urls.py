from django.urls import path
from app.views import *

urlpatterns = [
  path('rose/',rose,name ='rose'),
  path('apple/',apple,name='apple'),
]


