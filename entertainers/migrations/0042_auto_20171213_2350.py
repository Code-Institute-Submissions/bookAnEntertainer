# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0041_auto_20171213_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainer',
            name='image1',
            field=models.ImageField(default='media/no_image.png', upload_to='media/img1/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image2',
            field=models.ImageField(default='media/no_image.png', upload_to='media/img2/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image3',
            field=models.ImageField(default='media/no_image.png', upload_to='media/img3/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image4',
            field=models.ImageField(default='media/no_image.png', upload_to='media/img4/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image5',
            field=models.ImageField(default='media/no_image.png', upload_to='media/img5/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='profile_image',
            field=models.ImageField(default='media/no_image.png', upload_to='media/profile/%Y/%m/%d'),
        ),
    ]
