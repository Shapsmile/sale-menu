from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'calculator'
urlpatterns = [
    path('', get_calorie_rate, name='calorie_rate'),
]
