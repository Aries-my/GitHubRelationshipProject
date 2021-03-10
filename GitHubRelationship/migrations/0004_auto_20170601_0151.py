# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-31 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GitHubRelationship', '0003_auto_20170531_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaborate_duckduckgo_zeroclickinfo_goodies_edges',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='collaborate_jquery_jquery_edges',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='collaborate_netty_netty_edges',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='collaborate_puppetlabs_puppetdb_edges',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='collaborate_rails_rails_edges',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='collaborate_saltstack_salt_edges',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='commit_duckduckgo_zeroclickinfo_goodiesy_edges',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='commit_jquery_jquery_edges',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='commit_netty_netty_edges',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='commit_puppetlabs_puppetdb_edges',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='commit_rails_rails_edges',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='commit_saltstack_salt_edges',
            name='uid',
        ),
        migrations.AlterField(
            model_name='collaborate_duckduckgo_zeroclickinfo_goodies_edges',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='collaborate_jquery_jquery_edges',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='collaborate_netty_netty_edges',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='collaborate_puppetlabs_puppetdb_edges',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='collaborate_rails_rails_edges',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='collaborate_saltstack_salt_edges',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commit_duckduckgo_zeroclickinfo_goodiesy_edges',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commit_jquery_jquery_edges',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commit_netty_netty_edges',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commit_puppetlabs_puppetdb_edges',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commit_rails_rails_edges',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commit_saltstack_salt_edges',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
