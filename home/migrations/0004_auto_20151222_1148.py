# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import wagtail.wagtailcore.fields
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('home', '0003_auto_20151221_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 12, 22, 11, 48, 21, 55343, tzinfo=utc), verbose_name='Post date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='feed_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_nl',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='search_description_en',
            field=models.TextField(null=True, verbose_name='search description', blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='search_description_nl',
            field=models.TextField(null=True, verbose_name='search description', blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='seo_title_en',
            field=models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title', blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='seo_title_nl',
            field=models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title', blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slug_en',
            field=models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slug_nl',
            field=models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_nl',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title'),
        ),
    ]
