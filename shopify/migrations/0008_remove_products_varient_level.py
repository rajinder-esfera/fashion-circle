# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-11 10:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0007_auto_20171211_0500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='varient_level',
        ),
    ]