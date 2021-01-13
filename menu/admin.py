from django.contrib import admin
from .models import Menu, Week, Day, Meal, Dish


# admin.site.register(Menu)
# admin.site.register(Week)
# admin.site.register(Day)
# admin.site.register(Meal)
# admin.site.register(Dish)

class WeekInline(admin.TabularInline):
	model = Week


class MenuAdmin(admin.ModelAdmin):
	list_display = ('menu_name', 'min_calories', 'max_calories')
	fields = ['menu_name', ('min_calories', 'max_calories')]
	inlines = [WeekInline]

admin.site.register(Menu, MenuAdmin)


class DayInline(admin.TabularInline):
	model = Day


@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
	list_display = ('week_number', 'menu')
	list_filter = ('menu',)
	fields = ['week_number', 'menu']
	inlines = [DayInline]


class MealInline(admin.TabularInline):
	model = Meal
	extra = 0  # Не добавляет три пустых поля для добавления новых объектов

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
	list_display = ('day_name', 'week')
	list_filter = ('week',)
	fields = ['day_name', 'week']
	inlines = [MealInline]


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
	list_display = ('meal_name', 'day')
	list_filter = ('day',)
	fields = ['meal_name', 'day']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
	list_display = ('dish_name', 'calories_per_hundred')
