# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20170611_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='author_img',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='topic',
            name='content',
            field=models.TextField(default=None),
        ),
    ]
