# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 09:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopcat', '0002_auto_20181025_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_Time', models.DateTimeField(auto_now_add=True)),
                ('recv_name', models.CharField(max_length=100, verbose_name='收件人')),
                ('recv_tel', models.CharField(max_length=100, verbose_name='收件人电话')),
                ('recv_address', models.CharField(max_length=255, verbose_name='收件人地址')),
                ('all_price', models.FloatField(verbose_name='订单总金额')),
                ('remark', models.CharField(max_length=255, verbose_name='订单备注')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='订单所属用户')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('good_id', models.IntegerField(verbose_name='商品编号')),
                ('good_img', models.CharField(max_length=255, verbose_name='商品图片')),
                ('good_name', models.CharField(max_length=100, verbose_name='商品名称')),
                ('good_price', models.IntegerField(verbose_name='商品价格')),
                ('good_count', models.IntegerField(verbose_name='商品数量')),
                ('good_price_all', models.IntegerField(verbose_name='商品总价')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopcat.Order', verbose_name='订单')),
            ],
        ),
    ]
