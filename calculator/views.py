from django.shortcuts import render, redirect
from django.db.models import F
from .forms import CalorieForm
from menu.models import Menu, Client
from django.urls import reverse
from django.http import HttpResponseRedirect


def get_calorie_rate(request):
	if request.method == 'POST':
		form = CalorieForm(request.POST)
		if form.is_valid():
			calorie_rate = form.calculate_calorie_rate()
			name = form.cleaned_data['your_name']
			email = form.cleaned_data['your_email']
			client = Client.objects.create(name=name, email=email, calorie_rate=calorie_rate) 
			return redirect('calculator:show_calorie_rate', client_id=client.id)
	else:
		form = CalorieForm()
	return render(request, template_name='calculator/calculator.html', context={'form': form})


def show_calorie_rate(request, client_id):
	client = Client.objects.get(id=client_id)
	cal_rate = client.calorie_rate
	menu = Menu.objects.filter(max_calories__gte=cal_rate).filter(min_calories__lt=cal_rate)[0]
	context = {
		'client': client,
		'menu': menu,
	}
	return render(request, template_name='calculator/show_calorie_rate.html', context=context)
