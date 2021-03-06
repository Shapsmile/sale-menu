# Generated by Django 3.1.4 on 2021-01-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20210105_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('calorie_content', models.PositiveIntegerField()),
                ('meal', models.ManyToManyField(to='menu.Meal')),
            ],
        ),
    ]
