# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0015_auto_20171122_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainer',
            name='image1',
            field=models.ImageField(default='media/no_image.png', upload_to='media/'),
        ),
    ]