# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0011_auto_20171122_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='entertainer',
            name='influences',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='entertainer',
            name='set_list',
            field=models.TextField(default='All genres and decades.'),
        ),
        migrations.AddField(
            model_name='entertainer',
            name='set_up_requirements',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Power Source', 'Power Source'), ('Stage Cover - If Outside', 'Stage Cover - If Outside'), ('Accomodation', 'Accomodation'), ('Food', 'Food'), ('Beverages', 'Beverages')], default='Power Source', max_length=65),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='description',
            field=models.CharField(choices=[('Band', 'Band'), ('Solo', 'Solo')], default='Band', max_length=14),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='genre',
            field=models.CharField(choices=[('Rock', 'Rock'), ('Metal', 'Metal'), ('Punk', 'Punk'), ('Blues', 'Blues'), ('Jazz', 'Jazz'), ('Classical', 'Classical'), ('Reggae', 'Reggae'), ('Ska', 'Ska'), ('Dance', 'Dance'), ('Funk', 'Funk')], default='Rock', max_length=9),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='location',
            field=models.CharField(choices=[('Antrim', 'Antrim'), ('Armagh', 'Armagh'), ('Carlow', 'Carlow'), ('Cavan', 'Cavan'), ('Clare', 'Clare'), ('Cork', 'Cork'), ('Derry', 'Derry'), ('Donegal', 'Donegal'), ('Down', 'Down'), ('Dublin', 'Dublin'), ('Fermanagh', 'Fermanagh'), ('Galway', 'Galway'), ('Kerry', 'Kerry'), ('Kildare', 'Kildare'), ('Kilkenny', 'Kilkenny'), ('Laois', 'Laois'), ('Leitrim', 'Leitrim'), ('Limerick', 'Limerick'), ('Longford', 'Longford'), ('Louth', 'Louth'), ('Mayo', 'Mayo'), ('Meath', 'Meath'), ('Monaghan', 'Monaghan'), ('Offaly', 'Offaly'), ('Roscommon', 'Roscommon'), ('Sligo', 'Sligo'), ('Tipperary', 'Tipperary'), ('Tyrone', 'Tyrone'), ('Waterford', 'Waterford'), ('Westmeath', 'Westmeath'), ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow')], default='Antrim', max_length=10),
        ),
    ]
