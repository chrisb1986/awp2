# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
