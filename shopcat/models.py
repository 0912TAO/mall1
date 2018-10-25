from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from goods.models import Goods


# 购物车
class ShopCart(models.Model):
    # 购物编号
    id = models.AutoField(primary_key=True)
    # 购物车商品
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="购物车商品")
    # 商品数量
    count = models.IntegerField(default=1, verbose_name="商品数量")
    # 商品添加时间
    addTime = models.DateTimeField(auto_now_add=True, verbose_name="商品添加时间")
    # 小计金额
    allTotal = models.FloatField()
    # 添加者
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='购物车所属用户')
