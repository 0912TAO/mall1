from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^my_cart/$', views.my_cart, name='my_cart'),
    url(r'^open_shop/$', views.open_shop, name='open_shop'),

]