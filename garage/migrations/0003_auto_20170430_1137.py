# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0002_variation_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_model',
            name='car_image',
            field=models.FileField(upload_to=''),
        ),
    ]
