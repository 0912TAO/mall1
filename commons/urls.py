from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^code/$', views.code, name='code'),
    url(r'^shouji/$', views.shouji, name='shouji'),
    url(r'^jiadian/$', views.jiadian, name='jiadian'),
    url(r'^peijian/$', views.peijian, name='peijian'),
    url(r'^shuma/$', views.shuma, name='shuma'),
    url(r'^pub/$', views.pub, name='pub'),

]