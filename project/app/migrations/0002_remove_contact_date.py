# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2021-04-14 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]