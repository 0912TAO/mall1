from django.conf.urls import url

from . import views

urlpatterns = [
    # 商品购买
    url(r'^product/$', views.product, name="product"),
]