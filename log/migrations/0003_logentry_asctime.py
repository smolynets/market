# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-30 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_remove_logentry_asctime'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='asctime',
            field=models.DateTimeField(null=True),
        ),
    ]