# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-18 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_scopuskatalog_journal'),
    ]

    operations = [
        migrations.AddField(
            model_name='scopuskatalog',
            name='citescore',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='scopuskatalog',
            name='sjr',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='scopuskatalog',
            name='snip',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
