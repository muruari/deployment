# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20180331_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='exam.User'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trips',
            field=models.ManyToManyField(default=None, related_name='joined', to='exam.User'),
        ),
    ]
