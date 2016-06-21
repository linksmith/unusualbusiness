# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20160620_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticlepage',
            name='format',
            field=models.CharField(choices=[(b'images', 'Image slideshow'), (b'audio', 'Audio embed'), (b'video', 'Video embed')], default=(b'event', 'Event'), max_length=32, verbose_name='page_format'),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='format',
            field=models.CharField(choices=[(b'text', 'Normal Article'), (b'audio', 'Audio embed'), (b'video', 'Video embed'), (b'images', 'Image slideshow')], default=(b'text', 'Normal Article'), max_length=32, verbose_name='page_format'),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='format',
            field=models.CharField(choices=[(b'theory', 'Theory Article'), (b'audio', 'Audio embed'), (b'video', 'Video embed')], default=(b'theory', 'Theory Article'), max_length=32, verbose_name='page_format'),
        ),
    ]