from django.db import models

# Create your models here.


# 引入内置user表
from django.contrib.auth.models import User


# 用户数据
class UserA(models.Model):
    uid = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, default="未设置", verbose_name='用户电话')
    umaney = models.CharField(max_length=255, verbose_name="用户余额")
    age = models.IntegerField(default=1, verbose_name='用户年龄')
    # 默认是0表示保密，1表示男生，2表示女生
    gender = models.CharField(max_length=10, default=0, verbose_name='用户性别')
    header = models.ImageField(upload_to="static/images/headers", default="static/images/default.jpg", verbose_name='用户头像')

    collection = models.CharField(max_length=255, verbose_name="用户收藏店铺")
    add = models.CharField(max_length=500, verbose_name="用户收货地址")

    user = models.OneToOneField(User, on_delete=models.CASCADE)


# 收货地址
class Address(models.Model):
    # 地址编号
    id = models.AutoField(primary_key=True)
    # 收货人
    recr_name = models.CharField(max_length=100,verbose_name="收货人")
    # 收货人电话
    recr_tel = models.CharField(max_length=20,verbose_name="收货人的电话号码")
    # 收货人所在省份
    province = models.CharField(max_length=100,verbose_name="收货人所在省份")
    # 收货人所在城市
    city = models.CharField(max_length=100,verbose_name="收货人所在城市")
    # 收货人所在区县
    area = models.CharField(max_length=100,verbose_name="收货人所在区县")
    # 收货人详细地址
    street = models.CharField(max_length=100,verbose_name="收货人详细地址")
    # 邮政编码
    postal = models.IntegerField(verbose_name="邮政编码")
    # 地址标签
    add_label = models.CharField(max_length=20,verbose_name="地址标签")  #0 家 1 公司 2 学校
    # 默认地址
    is_default = models.BooleanField(default=False,verbose_name="默认地址")# Flase 默认地址，True 非默认地址
    # 地址所属用户
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="地址所属用户")