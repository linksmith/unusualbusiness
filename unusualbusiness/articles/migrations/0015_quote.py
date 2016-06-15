# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_delete_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(help_text='A quote from an article.', max_length=255, verbose_name='Quote')),
                ('author', models.CharField(blank=True, help_text='Whom is this quote attributed to.', max_length=255, verbose_name='Attribution')),
                ('link', models.URLField(blank=True, help_text='Click quote to go to link.', max_length=255, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Quote',
                'verbose_name_plural': 'Quotes',
            },
        ),
    ]