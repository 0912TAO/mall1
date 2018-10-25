from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from goods.models import Goods


# 购物车
class ShopCart(models.Model):
    # 购物编号
    id= models.AutoField(primary_key=True)
    # 购物车商品
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE ,verbose_name="购物车商品")
    # 商品数量
    count = models.IntegerField(verbose_name="商品数量")
    # 商品添加时间
    addTime = models.DateTimeField(auto_now_add=True,verbose_name="商品添加时间")
    # 小计金额
    allTotal = models.FloatField()
    # 添加者
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="购物车所属用户")

# 订单
class Order(models.Model):
    # 订单编号
    id = models.AutoField(primary_key=True)
    # 所属用户
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="订单所属用户")
    # 下单时间
    create_Time = models.DateTimeField(auto_now_add=True)
    # 收件人
    recv_name = models.CharField(max_length=100,verbose_name="收件人")
    # 收件人电话
    recv_tel = models.CharField(max_length=100,verbose_name="收件人电话")
    # 收件人地址
    recv_address = models.CharField(max_length=255,verbose_name="收件人地址")
    # 总金额
    all_price = models.FloatField(verbose_name="订单总金额")
    # 订单备注
    remark = models.CharField(max_length=255,verbose_name="订单备注")


# 总订单单项
class OrderItem(models.Model):
    # 单项订单编号
    id = models.AutoField(primary_key=True)
    # 商品编号
    good_id= models.IntegerField(verbose_name="商品编号")
    # 商品图片
    good_img= models.CharField(max_length=255,verbose_name="商品图片")
    # 商品名称
    good_name= models.CharField(max_length=100,     verbose_name="商品名称")
    # 商品价格
    good_price = models.IntegerField(verbose_name="商品价格")
    # 商品价格
    good_count = models.IntegerField(verbose_name="商品数量")
    # 商品总价
    good_price_all = models.IntegerField(verbose_name="商品总价")
    #
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="订单")