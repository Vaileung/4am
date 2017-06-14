# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Category'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]