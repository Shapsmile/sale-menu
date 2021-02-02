from django import forms
from .models import Dish


class DishForm(forms.ModelForm):
	class Meta:
		model = Dish
		fields = [
			'dish_name',
			'ingredients',
			'calories_per_hundred',
		]
		labels = {
			'dish_name': 'Название',
			'ingredients': 'Состав',
			'calories_per_hundred': 'Калорийность на 100 гр. продукта, ккал',
		}
		widgets = {
			'dish_name': forms.TextInput(attrs={'class': 'form-control'}),
			'ingredients': forms.Textarea(attrs={'class': 'form-control'}),
			'calories_per_hundred': forms.NumberInput(attrs={'class': 'form-control'}),
		}
