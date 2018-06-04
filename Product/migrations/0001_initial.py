# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-13 08:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(default='UAH', max_length=5)),
                ('description', models.TextField()),
                ('date_of_publishing', models.DateField(blank=True, default=datetime.datetime.now)),
                ('date_of_adding', models.DateField(auto_now=True)),
            ],
        ),
    ]
