# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-02-17 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='photo_big',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='flower',
            name='photo_main',
            field=models.ImageField(upload_to=''),
        ),
    ]
