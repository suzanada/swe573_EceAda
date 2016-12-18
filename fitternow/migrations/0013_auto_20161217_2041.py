# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-17 20:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitternow', '0012_userconsumption'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconsumption',
            name='user_cons_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userconsumption',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
