# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-07 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0002_auto_20171005_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(help_text='Example: appetizer, main course, dessert', max_length=150, verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Dish Name'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Meal Name'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Timetable Name'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Vendor Name'),
        ),
    ]