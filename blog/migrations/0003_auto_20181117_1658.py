# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-17 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(blank=True, default='code.png', upload_to=b''),
        ),
    ]