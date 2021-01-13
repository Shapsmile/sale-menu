from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse


"""Модель недели. В идеале к неделе должны привязываться 7 дней,
	к каждму из которых привязывается 4 приема пищи, соответственно, в 
	каждый из которых привязывается блюда количество которых не ограничено.
	Нужно что бы калорийность блюд суммировалась в калорийность приема пищи, 
	далее калорийность приемов пищи суммируется в калорийность дня. 
	В итоге калорийность недели это сумма всех калорий."""


class Menu(models.Model):
	"""Модель меню"""
	menu_name = models.CharField(max_length=50)
	min_calories = models.IntegerField()
	max_calories = models.IntegerField()	

	def __str__(self):
		return self.menu_name

	def get_absolute_url(self):
		return reverse('menu:menu_detail', kwargs={'menu_id': self.pk})


class Week(models.Model):
	"""Модель недели"""
	menu = models.ForeignKey('Menu', on_delete=models.SET_NULL, blank=True, null=True)
	week_number = models.SlugField(allow_unicode=True)

	def __str__(self):
		return self.week_number

	def get_absolute_url(self):
		return reverse('menu:week_detail', kwargs={'week_id': self.pk})


class Day(models.Model):
	"""Модель дней недели"""
	week = models.ForeignKey('Week', on_delete=models.SET_NULL, blank=True, null=True)
	day_name = models.CharField(max_length=15)

	def display_menu(self):
		return Day.objects.values('week__menu__menu_name').get(id=self.id)

	def __str__(self):
		return self.day_name


class Meal(models.Model):
	"""Модель приема пищи, например, завтрак, обед и т.д."""
	meal_name = models.CharField(max_length=15)
	day = models.ForeignKey('Day', on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return self.meal_name


class Dish(models.Model):
	"""Модель блюда"""
	dish_name = models.CharField(max_length=100)
	ingredients = models.TextField(default=None)
	meals = models.ManyToManyField(Meal)
	calories_per_hundred = models.PositiveIntegerField()
	weight = models.FloatField(default=0)

	def __str__(self):
		return self.dish_name

		

