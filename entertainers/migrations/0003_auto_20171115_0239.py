# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
         ('entertainers', '0002_auto_20171115_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='entertainer',
            name='location',
            field=models.CharField(choices=[('ANTRIM', 'Antrim'), ('ARMAGH', 'Armagh'), ('CARLOW', 'Carlow'), ('CAVAN', 'Cavan'), ('CLARE', 'Clare'), ('CORK', 'Cork'), ('DERRY', 'Derry'), ('DONEGAL', 'Donegal'), ('DOWN', 'Down'), ('DUBLIN', 'Dublin'), ('FERMANAGH', 'Fermanagh'), ('GALWAY', 'Galway'), ('KERRY', 'Kerry'), ('KILDARE', 'Kildare'), ('KILKENNY', 'Kilkenny'), ('LAOIS', 'Laois'), ('LEITRIM', 'Leitrim'), ('LIMERICK', 'Limerick'), ('LONGFORD', 'Longford'), ('LOUTH', 'Louth'), ('MAYO', 'Mayo'), ('MEATH', 'Meath'), ('MONAGHAN', 'Monaghan'), ('OFFALY', 'Offaly'), ('ROSCOMMON', 'Roscommon'), ('SLIGO', 'Sligo'), ('TIPPERARY', 'Tipperary'), ('TYRONE', 'Tyrone'), ('WATERFORD', 'Waterford'), ('WESTMEATH', 'Westmeath'), ('WEXFORD', 'Wexford'), ('WICKLOW', 'Wicklow')], default='ANTRIM', max_length=10),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='description',
            field=models.CharField(choices=[('BAND', 'Band'), ('SOLO_MUSICIAN', 'Solo Musician')], default='BAND', max_length=4),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='genre',
            field=models.CharField(choices=[('ROCK', 'Rock'), ('METAL', 'Metal'), ('PUNK', 'Punk'), ('BLUES', 'Blues'), ('JAZZ', 'Jazz'), ('CLASSICAL', 'Classical'), ('REGGAE', 'Reggae'), ('SKA', 'Ska'), ('DANCE', 'Dance'), ('FUNK', 'Funk')], default='ROCK', max_length=4),
        ),
    ]