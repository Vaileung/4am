# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('topic', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=300)),
                ('cc_myself', models.BooleanField()),
            ],
            options={
                'ordering': ['subject'],
            },
        ),
    ]
