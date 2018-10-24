from django.db import models

# 引入用户
from django.contrib.auth.models import User


# Create your models here.
<<<<<<< HEAD
class store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,verbose_name="店铺名称")
    cover = models.ImageField(upload_to="store/static/cover/", default="store/static/cover/default.jpg", verbose_name="店铺封面")
    intro = models.TextField(verbose_name="店铺描述")
    # 0 表示店铺正常营业 1 表示暂停营业 2 表示永久歇业
    state = models.IntegerField(default=0, verbose_name="店铺状态")
    open_time = models.DateField(auto_now_add=True, verbose_name="开店时间")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="店铺所有者")
=======


from django.contrib.auth.models import User

class store(models.Model):
    # 店铺编号：
    id = models.AutoField(primary_key=True)
    # 店铺名称：
    name = models.CharField(max_length=20,verbose_name="店铺信息")
    # 店铺封面：
    cover = models.ImageField(upload_to="static/images/shop",default="static/images/default.jpg", verbose_name='店铺封面')
    # 店铺描述：
    intro = models.TextField()
    # 开店时间：
    opener_time = models.DateTimeField(auto_now_add=True)
    # 店铺状态：0 1 2 3
    status  = models.IntegerField(default=0,verbose_name="店铺状态")  #0 正常营业  1 暂停营业  2 删除店铺（永久删除）
    # 所属用户：
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="店铺所属用户")
>>>>>>> ca8defcd1c61002d02d2df97188c5d02789def04
