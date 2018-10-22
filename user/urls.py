from django.conf.urls import url

from . import views

urlpatterns = [
    # 登录
    url(r'^user_login/$', views.user_login, name='user_login'),

    # 注册
    url(r'^register/$', views.register, name='register'),

    # 验证验证码
    url(r'^(\w+)/checkcode/$', views.checkcode, name='checkcode'),

    # 验证密码是否正确
    url(r'^(\w+)/check_password/$', views.check_password, name='check_password'),

    # 个人中心
    url(r'^personal/$', views.personal, name='personal'),

    # 修改个人信息
    url(r'^changeinfo/$', views.changeinfo, name='changeinfo'),

    # 修改用户头像
    url(r'^changeheader/$', views.changeheader, name='changeheader'),

    # 验证旧密码
    url(r'^check_password/$', views.check_password, name='check_password'),

    # 修改用户密码
    url(r'^changepwd/$', views.changepwd, name='changepwd'),

    # 验证用户名是否存在
    url(r'^(\w+)/checkusername/$', views.checkusername, name='checkusername'),

    # 退出登录
    url(r'^user_logout/$', views.user_logout, name="user_logout"),
]