from django.conf.urls import url

from . import views

urlpatterns = [
    # 商品购买
    url(r'^product/$', views.product, name="product"),
    url(r'^add/$',views.add,name="add"),
    url(r'^findTypeByPID/$',views.findTypeByPID,name="findTypeByPID"),
    # 购买
    url(r'(?P<sp_id>\d+)/product/$', views.product, name="product"),
    # 评论
    url(r'(?P<goods_id>\d+)/pinglun/$', views.pinglun, name="pinglun"),
    # 详情
    url(r'(?P<goods_id>\d+)/xiangqing/$', views.xiangqing, name="xiangqing"),
]