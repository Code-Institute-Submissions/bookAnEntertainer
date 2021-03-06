# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 00:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0032_auto_20171203_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainer',
            name='set_list',
            field=models.TextField(default='Available on Request.'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
