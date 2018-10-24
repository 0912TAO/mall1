from django.shortcuts import render,redirect,reverse
from django.views.decorators.http import require_GET
from django.core.serializers import serialize
from django.http import HttpResponse
# Create your views here.

from . import models
from store.models import store

# 商品购买
def product(request):
    return render(request, "goods/product.html", {})


# 商品添加
def add(request):
    if request.method == "GET":
        return render(request,"goods/add.html",{})
    else:
        name = request.POST["name"]
        price = request.POST["price"]
        stock = request.POST["stock"]
        store_id = request.POST["store"]
        type2 = request.POST["type2"]
        intro = request.POST["intro"]
        cover = request.FILES["cover"]
        stores = store.objects.get(pk=store_id)
        goodsType = models.GoodType.objects.get(pk=type2)
        # 保存商品
        goods = models.Goods(name=name,price=price,stock=stock,intro=intro,stores=stores,goodstype=goodsType)
        goods.save()
        # 保存商品图片
        goodImage = models.GoodsImage(path=cover,goods=goods)
        goodImage.save()
        return redirect(reverse("store:baobei",kwargs={"s_id":store_id}))

@require_GET
def findTypeByPID(request):
    parent_id = request.GET["parent_id"]
    type2s = models.GoodType.objects.filter(parent=parent_id)
    return HttpResponse(serialize("json",type2s))


def product(request):
    return render(request, "goods/product.html", {})
    # return redirect(reverse("goods:product"))


def xiangqing(request):
    return render(request, "goods/xiangqing.html", {})


def pinglun(request):
    return render(request, "goods/pinglun.html", {})
