# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_auto_20160529_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationpage',
            name='twitter',
            field=models.URLField(blank=True, verbose_name='Twitter'),
        ),
    ]