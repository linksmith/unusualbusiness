# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 10:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20160615_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staticcontent',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='staticcontent',
            name='title_nl',
        ),
    ]