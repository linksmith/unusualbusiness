# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 08:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20160512_1051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsarticlepage',
            options={'verbose_name': 'News or report article', 'verbose_name_plural': 'News or report articles'},
        ),
    ]