# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20170621_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='attachment',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='attachment',
            name='page_count',
            field=models.IntegerField(null=True),
        ),
    ]