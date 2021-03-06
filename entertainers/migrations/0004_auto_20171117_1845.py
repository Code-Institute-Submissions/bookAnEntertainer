# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0003_auto_20171115_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainer',
            name='genre',
            field=models.CharField(choices=[('ROCK', 'Rock'), ('METAL', 'Metal'), ('PUNK', 'Punk'), ('BLUES', 'Blues'), ('JAZZ', 'Jazz'), ('CLASSICAL', 'Classical'), ('REGGAE', 'Reggae'), ('SKA', 'Ska'), ('DANCE', 'Dance'), ('FUNK', 'Funk')], default='ROCK', max_length=9),
        ),
    ]
