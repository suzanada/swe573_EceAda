# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-10 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitternow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateTimeField(default='1900-01-22'),
        ),
    ]