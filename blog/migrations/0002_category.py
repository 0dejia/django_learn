# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_node', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
    ]
