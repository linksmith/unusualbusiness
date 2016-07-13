# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
        ('events', '0001_initial'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyarticlepageorganization',
            name='organization_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='story_article_page', to='organizations.OrganizationPage'),
        ),
        migrations.AddField(
            model_name='storyarticlepageorganization',
            name='story_article_page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizations', to='articles.StoryArticlePage'),
        ),
        migrations.AddField(
            model_name='storyarticlepage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='articles.AuthorPage', verbose_name='author'),
        ),
        migrations.AddField(
            model_name='newsarticlepage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='articles.AuthorPage', verbose_name='author'),
        ),
        migrations.AddField(
            model_name='newsarticlepage',
            name='event_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_article_page', to='events.EventPage'),
        ),
        migrations.AddField(
            model_name='authorpage',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='photo'),
        ),
    ]