# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20171201_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='flare',
            name='latitude',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flare',
            name='longitude',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
