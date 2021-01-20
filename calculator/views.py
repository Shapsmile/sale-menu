from django.shortcuts import render, redirect
from django.db.models import F
from .forms import CalorieForm
from menu.models import Menu
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def get_calorie_rate(request):
	# для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
	# если это запрос POST, нам нужно обработать данные формы
	if request.method == 'POST':
	# создаем экземпляр формы и заполняем его данными из запроса:
		form = CalorieForm(request.POST)
		if form.is_valid():
			# обрабатываем данные в form.cleaned_data по мере необходимости
			# ...
			# перенаправить на новый URL:
			# menu_id = int(form.cleaned_data['page'])
			cr = form.calculate_calorie_rate()
			target = Menu.objects.filter(max_calories__gte=cr).filter(min_calories__lt=cr)[0].id
			return redirect('menu:week_list', menu_id=target)

	# если GET (или любой другой метод) мы создадим пустую форму
	else:
		form = CalorieForm()

	return render(request, template_name='calculator/calculator.html', context={'form': form})


# def show_calorie_rate(request, menu_id, calorie_rate):
	# """
	# Получает результат расчета калорийности и выводит менюшку
	# """
	# calorie_rate = calorie_rate
	# weeks = Week.objects.filter(menu__id=menu_id)
	# menu = Menu.objects.get(pk=menu_id)
	# context = {
		# 'weeks': weeks,
		# 'menu': menu,
		# 'thing': thing,
	# }
	# return render(request, template_name='calculator/cal_rate_menu.html', context=context)