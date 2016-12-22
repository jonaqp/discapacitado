# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-19 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnireniec', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicioreniec',
            name='appservice',
            field=models.CharField(max_length=100, verbose_name='App'),
        ),
        migrations.AlterField(
            model_name='servicioreniec',
            name='namespace',
            field=models.CharField(max_length=250, verbose_name='NameSpace'),
        ),
        migrations.AlterField(
            model_name='servicioreniec',
            name='passservice',
            field=models.CharField(max_length=500, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='servicioreniec',
            name='urlwsdlservice',
            field=models.CharField(max_length=500, verbose_name='UrlWSLD'),
        ),
        migrations.AlterField(
            model_name='servicioreniec',
            name='userservice',
            field=models.CharField(max_length=8, verbose_name='User'),
        ),
    ]