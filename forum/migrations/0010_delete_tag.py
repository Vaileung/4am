# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 15:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20170626_1734'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
