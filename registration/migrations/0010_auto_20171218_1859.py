# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 13:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_auto_20171218_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='date',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]