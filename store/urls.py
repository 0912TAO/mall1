from django.conf.urls import url

from . import views

urlpatterns = [
    # 购物车
    url(r'^my_cart/$', views.my_cart, name='my_cart'),
    # 开店
    url(r'^open_shop/$', views.open_shop, name='open_shop'),
    # 确认订单
    url(r'^confirm/$', views.confirm, name='confirm'),
    # 结算页面
    url(r'^pay/$', views.pay, name='pay')

]