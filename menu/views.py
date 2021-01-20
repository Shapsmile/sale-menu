from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Menu, Week, Day, Meal, Dish
# from .forms import TagForm, PostForm
# from .utils import ObjectCreateMixin
from django.db.models import F, Sum, ExpressionWrapper, PositiveIntegerField


def index(request):
	menus = Menu.objects.all()
	context = {
		'menus': menus
	}
	return render(request, template_name='menu/menu_list.html', context=context)


def get_week_list(request, menu_id, **kwargs):
	thing = kwargs
	weeks = Week.objects.filter(menu__id=menu_id)
	menu = Menu.objects.get(pk=menu_id)
	context = {
		'weeks': weeks,
		'menu': menu,
		'thing': thing,
	}
	return render(request, template_name='menu/week_list.html', context=context)


def get_day_list(request, menu_id, week_id):
	days = Day.objects.filter(week__id=week_id)
	week = Week.objects.get(pk=week_id)
	menu = Menu.objects.get(pk=menu_id)
	context = {
		'days': days,
		'week': week,
		'menu': menu
	}
	return render(request, template_name='menu/day_list.html', context=context)


def get_meal_list(request, menu_id, week_id, day_id):
	meals = Meal.objects.filter(day__id=day_id)
	day = Day.objects.get(pk=day_id)
	week = Week.objects.get(pk=week_id)
	menu = Menu.objects.get(pk=menu_id)
	context = {
		'meals': meals,
		'day': day,
		'week': week,
		'menu': menu
	}
	return render(request, template_name='menu/meal_list.html', context=context)


def get_dish_list(request, menu_id, week_id, day_id, meal_id):
	# calorie_content = Dish.objects.filter(meals__meal_name=).annotate(calorie_content=ExpressionWrapper(
	# # 	F('weight')/100 * F('calories_per_hundred'), output_field=PositiveIntegerField()))
	dishes = Dish.objects.filter(meals__id=meal_id)
	total = Dish.objects.filter(
		meals__id=meal_id).annotate(
		calorie_content=ExpressionWrapper(
			F('weight')/100 * F('calories_per_hundred'), output_field=PositiveIntegerField())).aggregate(
		total=Sum('calorie_content'))['total']
	meal = Meal.objects.get(pk=meal_id)
	day = Day.objects.get(pk=day_id)
	week = Week.objects.get(pk=week_id)
	menu = Menu.objects.get(pk=menu_id)
	context = {
		'dishes': dishes,
		'meal': meal,
		'day': day,
		'week': week,
		'menu': menu,
		'total': total,
	}
	return render(request, template_name='menu/dish_list.html', context=context)


#
#
# class MenuDetailView(generic.DetailView):
# 	model = Menu
# 	template_name = 'menu/menu_detail.html'
# 	pk_url_kwarg = 'menu_id'
#
#
# class WeekDetailView(generic.DetailView):
# 	model = Week
# 	template_name = 'menu/week_detail.html'
# 	pk_url_kwarg = 'week_id'
