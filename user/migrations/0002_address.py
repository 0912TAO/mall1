# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 07:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recr_name', models.CharField(max_length=100, verbose_name='收货人')),
                ('recr_tel', models.CharField(max_length=20, verbose_name='收货人的电话号码')),
                ('province', models.CharField(max_length=100, verbose_name='收货人所在省份')),
                ('city', models.CharField(max_length=100, verbose_name='收货人所在城市')),
                ('area', models.CharField(max_length=100, verbose_name='收货人所在区县')),
                ('street', models.CharField(max_length=100, verbose_name='收货人详细地址')),
                ('postal', models.IntegerField(max_length=100, verbose_name='邮政编码')),
                ('add_label', models.CharField(max_length=20, verbose_name='地址标签')),
                ('is_default', models.BooleanField(default=False, verbose_name='默认地址')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='地址所属用户')),
            ],
        ),
    ]