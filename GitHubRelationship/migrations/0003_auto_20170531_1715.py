# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-31 09:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GitHubRelationship', '0002_auto_20170524_1304'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='users',
        ),
    ]
