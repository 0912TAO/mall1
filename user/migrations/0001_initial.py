# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 13:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserA',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(default='未设置', max_length=11, verbose_name='用户电话')),
                ('umaney', models.CharField(max_length=255, verbose_name='用户余额')),
                ('age', models.IntegerField(default=1, verbose_name='用户年龄')),
                ('gender', models.CharField(default=0, max_length=10, verbose_name='用户性别')),
                ('header', models.ImageField(default='static/images/default.jpg', upload_to='static/images/headers', verbose_name='用户头像')),
                ('collection', models.CharField(max_length=255, verbose_name='用户收藏店铺')),
                ('add', models.CharField(max_length=500, verbose_name='用户收货地址')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
