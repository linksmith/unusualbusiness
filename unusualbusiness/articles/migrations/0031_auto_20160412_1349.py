# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0030_auto_20160412_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())]),
        ),
        migrations.AlterField(
            model_name='reportarticlepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())], null=True),
        ),
        migrations.AlterField(
            model_name='reportarticlepage',
            name='body_nl',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())], null=True),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())]),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())], null=True),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='body_nl',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())], null=True),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())]),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())], null=True),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='body_nl',
            field=wagtail.wagtailcore.fields.StreamField([('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())], null=True),
        ),
    ]
