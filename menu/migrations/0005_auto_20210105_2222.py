# Generated by Django 3.1.4 on 2021-01-05 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20210105_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='meal',
            new_name='meals',
        ),
    ]
