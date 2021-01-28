from django import forms

GENDER_CHOICES = [
    ('1', 'Мужчина'),
    ('2', 'Женщина'),
]

ACTIVITY_COEFFICIENT = [
	('1.2', 'Минимальная активность'),
	('1.375', 'Слабая активность'),
	('1.55', 'Средняя активность'),
	('1.725', 'Высокая активность'),
	('1.9', 'Экстра-активность'),
]


class CalorieForm(forms.Form):
	your_name = forms.CharField(label= 'Ваше имя', max_length=50)
	your_email = forms.CharField(label= 'Ваш Email', max_length=50)
	your_age = forms.IntegerField(label='Ваш возраст')
	your_weigth = forms.IntegerField(label='Ваш вес')
	your_growth = forms.IntegerField(label='Ваш рост')
	your_gender = forms.ChoiceField(label='Ваш пол',
        required=False,
        widget=forms.RadioSelect,
        choices=GENDER_CHOICES,
    )
	active_coeff = forms.ChoiceField(label='Ваша активность',
        required=False,
        widget=forms.Select,
        choices=ACTIVITY_COEFFICIENT,
    )
	# page = forms.IntegerField(label='Номер меню')
	def calculate_calorie_rate(self):
		age = self.cleaned_data['your_age']
		weigth = self.cleaned_data['your_weigth']
		growth = self.cleaned_data['your_growth']
		gender = self.cleaned_data['your_gender']
		active_coeff = self.cleaned_data['active_coeff']
		if gender == '1':
			# для мужчин: (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) + 5) x A
			cal_rate = (10 * weigth + 6.25 * growth - 5 * age + 5) * float(active_coeff)
			return int(cal_rate)
		else:
			# для женщин: (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) – 161) x A.
			cal_rate = (10 * weigth + 6.25 * growth - 5 * age - 161) * float(active_coeff)
			return int(cal_rate)
