# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-26 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beat_exchange', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='suspend',
            field=models.BooleanField(default=False),
        ),
    ]
