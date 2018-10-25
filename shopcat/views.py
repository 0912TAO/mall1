from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
# Create your views here.
from goods.models import GoodType, Goods
import logging


# 添加购物车（参数值，商品数量，商品ID）
@require_GET
# @login_required
def add(request, count, goods_id):
    # GET方式打开页面
    # if request.method == 'GET':
    #     # 记录一条信息
    #     a = request.META['REMOTE_ADDR']
    #     logger = logging.getLogger('require_django')
    #     logger.info(a + '打开购物车')
    #
    #     goods = Goods.objects.get(pk=goods_id)
    #     return render(request, 'store/my_cart.html', {})
    #
    # # POST方式打开页面
    # elif request.method == 'POST':
    #     pass
    pass