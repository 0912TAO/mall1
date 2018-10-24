from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^my_cart/$', views.my_cart, name='my_cart'),
    url(r'^open_shop/$', views.open_shop, name='open_shop'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r"^list",views.list,name="list"),

    url(r"^(?P<s_id>\d+)/detail/",views.detail,name="detail"),
    url(r"^(?P<s_id>\d+)/update/",views.update,name="update"),
    url(r"^(?P<s_id>\d+)/(?P<status>\d+)/change/",views.change,name="change"),


]