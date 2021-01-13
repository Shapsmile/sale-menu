from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'menu'
urlpatterns = [
    path('', index, name='menu_list'),
    path('menu/<int:menu_id>/', get_week_list, name='week_list'),
    path('menu/<int:menu_id>/<int:week_id>', get_day_list, name='day_list'),
    path('menu/<int:menu_id>/<int:week_id>/<int:day_id>', get_meal_list, name='meal_list'),
    path('menu/<int:menu_id>/<int:week_id>/<int:day_id>/<int:meal_id>', get_dish_list, name='dish_list'),
]
