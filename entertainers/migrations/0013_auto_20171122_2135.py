# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0012_auto_20171122_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainer',
            name='influences',
            field=models.TextField(default='All Genres and decades.'),
        ),
    ]
