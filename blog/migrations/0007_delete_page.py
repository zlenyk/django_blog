# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 14:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_page_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Page',
        ),
    ]