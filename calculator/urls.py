from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'calculator'
urlpatterns = [
    path('', get_calorie_rate, name='calorie_rate'),
    path('calorie_menu/', show_calorie_rate, name='show_calorie_rate'),
]
