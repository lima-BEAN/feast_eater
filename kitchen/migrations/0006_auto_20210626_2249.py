# Generated by Django 3.2.4 on 2021-06-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0005_kitchen_working_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='close_time',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='open_time',
            field=models.CharField(max_length=10),
        ),
    ]
