from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
# Create your views here.



@require_GET
@login_required
# 添加购物车（参数值，商品数量，商品ID）
def add(request,count,goos_id):
    pass