from django.conf.urls import url

from . import views

urlpatterns = [
    # 购物车
    url(r'^my_cart/$', views.my_cart, name='my_cart'),
    # 开店
    url(r'^open_shop/$', views.open_shop, name='open_shop'),
    # url(r'^i_want_open_shop/$', views.i_want_open_shop, name='i_want_open_shop'),
    # 添加商铺
    url(r'^shop/$', views.shop, name='shop'),
    # 商铺列表
    # url(r"^list",views.list,name="list"),
    # 细节（店铺详情）
    url(r"^(?P<s_id>\d+)/detail/",views.detail,name="detail"),
    # 添加商品
    url(r"^release_goods/",views.detail,name="release_goods"),
    # 更新店铺数据
    url(r"^(?P<s_id>\d+)/update/",views.update,name="update"),
    # 店铺状态更改
    url(r"^(?P<s_id>\d+)/(?P<status>\d+)/change/",views.change,name="change"),
    # 确认订单
    url(r'^confirm/$', views.confirm, name='confirm'),
    # 结算页面
    url(r'^pay/$', views.pay, name='pay')


]