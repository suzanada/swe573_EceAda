# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitternow', '0008_activity_useractivities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='id',
        ),
        migrations.AddField(
            model_name='activity',
            name='act_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
