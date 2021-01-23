from django.shortcuts import render, redirect
from django.db.models import F
from .forms import CalorieForm
from menu.models import Menu
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def get_calorie_rate(request):
	# если это запрос POST, нам нужно обработать данные формы
	if request.method == 'POST':
	# создаем экземпляр формы и заполняем его данными из запроса:
		form = CalorieForm(request.POST)
		if form.is_valid():
			# обрабатываем данные в form.cleaned_data по мере необходимости
			# ...
			# перенаправить на новый URL:
			calorie_rate = form.calculate_calorie_rate()
			menu_id = Menu.objects.filter(max_calories__gte=calorie_rate).filter(min_calories__lt=calorie_rate)[0].id
			menu = Menu.objects.get(id=menu_id)
			context = {
				'calorie_rate': calorie_rate,
				'menu': menu,
			}
			return render(request, 'calculator/show_calorie_rate.html', context)
	# если GET (или любой другой метод) мы создадим пустую форму
	else:
		form = CalorieForm()
	return render(request, template_name='calculator/calculator.html', context={'form': form})


def show_calorie_rate(request, **kwargs):
	"""
	Получает результат расчета калорийности и выводит менюшку
	"""
	# calorie_rate = calorie_rate
	# weeks = Week.objects.filter(menu__id=menu_id)
	menu = Menu.objects.get(pk=menu_id)
	context = {
		'weeks': weeks,
		'menu': menu,
		'thing': thing,
	}
	return render(request, template_name='calculator/show_calorie_rate.html')