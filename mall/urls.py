"""mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

# import xadmin
# from xadmin.plugins import xversion
# xadmin.autodiscover()
# xversion.register_models()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^xadmin/', xadmin.site.urls),

    url(r'^', include('commons.urls', namespace='commons')),
    url(r'^user/', include('user.urls', namespace='user')),
    url(r'^store/', include('store.urls', namespace='store')),
    url(r'^goods/', include('goods.urls', namespace='goods')),
    url(r'^commons/', include('commons.urls', namespace='commons')),

]

