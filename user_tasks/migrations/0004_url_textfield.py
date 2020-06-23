# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 17:51


import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_tasks', '0003_url_max_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertaskartifact',
            name='url',
            field=models.TextField(blank=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
