# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 10:20
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20160530_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='description',
            field=wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon='italic')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))]))], default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='description_en',
            field=wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon='italic')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))]))], null=True),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='description_nl',
            field=wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon='italic')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock()), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))]))], null=True),
        ),
    ]
