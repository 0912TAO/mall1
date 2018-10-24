from django.conf.urls import url

from . import views

urlpatterns = [
    # 购物车
    url(r'^my_cart/$', views.my_cart, name='my_cart'),
    # 开店
    url(r'^open_shop/$', views.open_shop, name='open_shop'),
<<<<<<< HEAD

=======
<<<<<<< HEAD
    url(r'^i_want_open_shop/$', views.i_want_open_shop, name='i_want_open_shop'),
=======
<<<<<<< HEAD
>>>>>>> 3b102c1f87cde6f2b626b5c8b867bd8c54d52147
    url(r'^shop/$', views.shop, name='shop'),
    url(r"^list",views.list,name="list"),

    url(r"^(?P<s_id>\d+)/detail/",views.detail,name="detail"),
    url(r"^(?P<s_id>\d+)/update/",views.update,name="update"),
    # 店铺状态更改
    url(r"^(?P<s_id>\d+)/(?P<status>\d+)/change/",views.change,name="change"),


    # 确认订单
    url(r'^confirm/$', views.confirm, name='confirm'),
    # 结算页面
    url(r'^pay/$', views.pay, name='pay')
<<<<<<< HEAD

=======
>>>>>>> bad801507888049a45a0e9f338bc8fb8cda42e39
>>>>>>> ca8defcd1c61002d02d2df97188c5d02789def04
>>>>>>> 3b102c1f87cde6f2b626b5c8b867bd8c54d52147

]