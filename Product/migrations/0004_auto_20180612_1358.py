# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20180612_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='about_brand',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='cizing',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='shipping',
            field=models.TextField(default=True),
        ),
    ]
