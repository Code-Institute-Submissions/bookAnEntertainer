# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0005_auto_20171117_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entertainer',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='entertainer',
            name='location',
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
