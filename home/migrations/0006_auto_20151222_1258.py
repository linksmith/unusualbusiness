# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20151222_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='stream',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('person', wagtail.wagtailcore.blocks.StructBlock([('first_name', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('surname', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('biography', wagtail.wagtailcore.blocks.RichTextBlock())], icon='user')), ('ingredients_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label='Ingredient')))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='stream_en',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('person', wagtail.wagtailcore.blocks.StructBlock([('first_name', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('surname', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('biography', wagtail.wagtailcore.blocks.RichTextBlock())], icon='user')), ('ingredients_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label='Ingredient')))], null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='stream_nl',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('person', wagtail.wagtailcore.blocks.StructBlock([('first_name', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('surname', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('biography', wagtail.wagtailcore.blocks.RichTextBlock())], icon='user')), ('ingredients_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label='Ingredient')))], null=True),
        ),
    ]
