# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-24 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinestore', '0004_auto_20181121_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='items'),
        ),
    ]
