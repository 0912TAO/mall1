# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodtype',
            name='cover',
            field=models.ImageField(default='static/images/goods/default.jpg', upload_to='static/images/goods', verbose_name='商品展示图片'),
        ),
    ]
