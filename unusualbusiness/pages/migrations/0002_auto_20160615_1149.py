# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralPageStaticContentPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('general_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='static_content_placements', to='pages.GeneralPage')),
            ],
            options={
                'verbose_name': 'Static content placement',
                'verbose_name_plural': 'Static content placements',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(help_text='A quote from an article.', max_length=255, verbose_name='Quote')),
                ('author', models.CharField(blank=True, help_text='Whom is this quote attributed to.', max_length=255, verbose_name='Attribution')),
                ('link', models.URLField(blank=True, help_text='Click quote to go to link.', max_length=255, null=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Quote',
                'verbose_name_plural': 'Quotes',
            },
        ),
        migrations.CreateModel(
            name='StaticContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Static HTML content for placement in pages', max_length=255, verbose_name='Title')),
                ('body', models.TextField(help_text='Static HTML content for placement in pages', verbose_name='HTML Body')),
            ],
            options={
                'verbose_name': 'Static content',
                'verbose_name_plural': 'Static contents',
            },
        ),
        migrations.AddField(
            model_name='generalpagestaticcontentplacement',
            name='static_content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pages.StaticContent'),
        ),
    ]