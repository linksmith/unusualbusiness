# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_nl',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='search_description_en',
            field=models.TextField(null=True, verbose_name='Search description', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='search_description_nl',
            field=models.TextField(null=True, verbose_name='Search description', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='seo_title_en',
            field=models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='Page title', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='seo_title_nl',
            field=models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='Page title', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slug_en',
            field=models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slug_nl',
            field=models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_nl',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='url_path_en',
            field=models.TextField(verbose_name='URL path', null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='url_path_nl',
            field=models.TextField(verbose_name='URL path', null=True, editable=False, blank=True),
        ),
    ]
