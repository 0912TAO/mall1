# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='postal',
            field=models.IntegerField(verbose_name='邮政编码'),
        ),
    ]
