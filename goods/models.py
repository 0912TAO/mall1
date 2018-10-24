from django.db import models

# Create your models here.
from store.models import store

import store

# 商品类型
class GoodType(models.Model):
    # 商品ID
    id = models.AutoField(primary_key=True)
    # 商品类型名称
    name  = models.CharField(max_length=255,unique=True,verbose_name="商品类型名称")
    # 商品展示图片
    cover = models.ImageField(upload_to="static/images/goods", default="static/images/goods/default.jpg", verbose_name="商品展示图片")
    # 商品类型描述
    intro = models.TextField(verbose_name="商品类别描述")
    # 关联类型（商品类型自关联）
    parent = models.ForeignKey("self",null=True,blank=True,verbose_name="父级类型",on_delete=models.CASCADE)


# 商品
class Goods(models.Model):
    # 商品编号：
    id = models.AutoField(primary_key=True)
    # 商品名称
    name = models.CharField(max_length=255,unique=True,verbose_name="商品名称")
    # 商品单价
    price = models.FloatField(verbose_name="商品单价")
    # 商品库存
    stock = models.IntegerField()
    # 销售数量
    count = models.IntegerField(default=0)# 默认第一次上架
    # 上架时间
    creatTime = models.DateTimeField(auto_now_add=True)
    # 商品介绍
    intro =  models.TextField(verbose_name="商品描述")
    # 商品所属商店
    stores = models.ForeignKey(store.models.store,on_delete=models.CASCADE,verbose_name="商品所属商店")
    # 商品所属类型
    goodstype = models.ForeignKey(GoodType,on_delete=models.CASCADE,verbose_name="商品所属类型")


# 商品图片类型
class GoodsImage(models.Model):
    # 商品图片ID
    id = models.AutoField(primary_key=True)
    # 商品图片存储路径
    path = models.ImageField(upload_to="static/images/goods", default="static/images/default.jpg",verbose_name="商品图片")
    # 图片显示
    status = models.BooleanField(default=False,verbose_name="是否默认展示图片")
    # 商品描述
    intro = models.TextField(verbose_name="商品图片描述",null=True,blank=True)
    # 图片所属商品
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="所属商品")
