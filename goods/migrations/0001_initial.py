# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='商品名称')),
                ('price', models.FloatField(verbose_name='商品单价')),
                ('stock', models.IntegerField()),
                ('count', models.IntegerField(default=0)),
                ('creatTime', models.DateTimeField(auto_now_add=True)),
                ('intro', models.TextField(verbose_name='商品描述')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.ImageField(default='static/images/default.jpg', upload_to='static/images/goods', verbose_name='商品图片')),
                ('status', models.BooleanField(default=False, verbose_name='是否默认展示图片')),
                ('intro', models.TextField(blank=True, null=True, verbose_name='商品图片描述')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='所属商品')),
            ],
        ),
        migrations.CreateModel(
            name='GoodType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='商品类型名称')),
                ('cover', models.ImageField(default='static/images/goods/default.jpg', upload_to='static/images/goods', verbose_name='商品展示图片')),
                ('intro', models.TextField(verbose_name='商品类别描述')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodType', verbose_name='父级类型')),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='goodstype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodType', verbose_name='商品所属类型'),
        ),
        migrations.AddField(
            model_name='goods',
            name='stores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store', verbose_name='商品所属商店'),
        ),
    ]
