# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-11 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitternow', '0004_auto_20161211_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.FloatField(default=170),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.FloatField(default=60),
        ),
    ]
