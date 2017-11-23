# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0022_auto_20171123_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainer',
            name='image1',
            field=models.ImageField(default='media/no_image.png', upload_to='media/img1/'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image2',
            field=models.ImageField(default='media/no_image.png', upload_to='media/img2/'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image3',
            field=models.ImageField(default='media/no_image.png', upload_to='media/img3/'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image4',
            field=models.ImageField(default='media/no_image.png', upload_to='media/img4/'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image5',
            field=models.ImageField(default='media/no_image.png', upload_to='media/img5/'),
        ),
    ]