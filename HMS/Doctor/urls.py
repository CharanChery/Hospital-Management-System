from django.urls import path
from .views import *


app_name = 'Doctor'

urlpatterns = [
    path('',dashboard,name='doctordashboard'),
]