# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-11 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborate_netty_netty_edges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(default=0)),
                ('target', models.IntegerField(verbose_name='target')),
                ('source', models.IntegerField(verbose_name='source')),
                ('weight', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Collaborate_netty_netty_nodes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('label', models.TextField(max_length=256)),
                ('modularity', models.IntegerField(default=0)),
                ('degree', models.IntegerField(default=0)),
                ('inDegree', models.IntegerField(default=0)),
                ('outDegree', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Commit_netty_netty_edges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(default=0)),
                ('target', models.IntegerField(verbose_name='target')),
                ('source', models.IntegerField(verbose_name='source')),
                ('weight', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Commit_netty_netty_nodes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('label', models.TextField(max_length=256)),
                ('modularity', models.IntegerField(default=0)),
                ('degree', models.IntegerField(default=0)),
                ('inDegree', models.IntegerField(default=0)),
                ('outDegree', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='follow_edges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField(verbose_name='target')),
                ('source', models.IntegerField(verbose_name='source')),
            ],
        ),
        migrations.CreateModel(
            name='follow_nodes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('label', models.TextField(max_length=256)),
                ('modularity', models.IntegerField(default=0)),
                ('degree', models.IntegerField(default=0)),
                ('inDegree', models.IntegerField(default=0)),
                ('outDegree', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='follow_edges',
            unique_together=set([('target', 'source')]),
        ),
        migrations.AlterUniqueTogether(
            name='commit_netty_netty_edges',
            unique_together=set([('target', 'source')]),
        ),
        migrations.AlterUniqueTogether(
            name='collaborate_netty_netty_edges',
            unique_together=set([('target', 'source')]),
        ),
    ]
