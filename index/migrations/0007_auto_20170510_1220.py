# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20170510_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='email',
        ),
        migrations.AddField(
            model_name='choice',
            name='id',
            field=models.AutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
