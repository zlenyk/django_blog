# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='content',
        ),
    ]
