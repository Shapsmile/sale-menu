# Generated by Django 3.1.4 on 2021-01-28 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20210113_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='Shapsmile@mail.ru', max_length=254)),
                ('calorie_rate', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
