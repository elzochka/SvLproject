# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_auto_20180612_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cizing',
            new_name='sizing',
        ),
    ]