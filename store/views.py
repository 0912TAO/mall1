from django.shortcuts import render,reverse,redirect
from django.contrib.auth.decorators import login_required   # 需要登陆的装饰器
from django.shortcuts import render,redirect,reverse
from django.views.decorators.http import require_GET
from . import models
import logging

from goods.models import GoodType, Goods


# 我的购物车
def my_cart(request):
    # GET方式打开页面
    if request.method == 'GET':
        # 记录一条信息
        a = request.META['REMOTE_ADDR']
        logger = logging.getLogger('require_django')
        logger.info(a + '打开购物车')
        return render(request, 'store/my_cart.html', {})

    # POST方式打开页面
    elif request.method == 'POST':
        pass



@login_required
# 开店
def open_shop(request):
    print("*****")
    try:
        store = models.store.objects.get(user_id=request.user.id)
        print(store)
        return render(request, 'store/open_shop.html', {"store": store})
    except:
        store = models.store.objects.filter(user_id=request.user.id)
        return render(request, 'store/open_shop.html', {"store": store})


# 添加商铺
@login_required()
def shop(request):
    if request.method == "GET":
        return render(request,'store/shop.html',{})
    else:
        name = request.POST["name"].strip()
        intro = request.POST["intro"].strip()
        try:
            cover = request.FILES["cover"]
            store1 = models.store(name=name,intro=intro,cover=cover,user=request.user)
        except:
            store1 = models.store(name=name, intro=intro,user=request.user)

        store1.save()
        # return redirect(reverse("store:list"))
        return redirect(reverse("store:detail",kwargs={"s_id":store1.id}))


# 商铺列表
# @require_GET
# @login_required()
# def list(request):
#     stores = models.store.objects.filter(user=request.user,status__in =[0,1])
#     return render(request,"store/list.html",{"stores":stores})


# 细节（店铺详情）
@require_GET
@login_required()
def detail(request,s_id):
    store = models.store.objects.get(pk=s_id)
    type1 = GoodType.objects.filter(parent__isnull=True)
    goods = Goods.objects.filter(stores=store)
    return render(request,"store/detail.html",{"store":store,"type1":type1,"goods":goods})


# 店铺状态更改
@login_required()
def change(request,s_id,status):
    store = models.store.objects.get(id=s_id)
    store.status = int(status)
    store.save()
    if store.status == 2:
        return redirect(reverse("store:open_shop"))
    else:
        return render(request, "store/open_shop.html", {"store": store})


# 永久删除
def delete(request,s_id):
    pass


# 更新数据
@login_required()
def update(request,s_id):

    if request.method == "GET":
        store = models.store.objects.get(pk=s_id)
        print(store.name)
        return render(request, "store/update.html", {"store": store})
    else:
        name = request.POST["name"].strip()
        intro = request.POST["intro"].strip()
        store = models.store.objects.get(pk=s_id)

        store.name = name
        store.intro = intro
        try:
            cover = request.FILES["cover"]
            store.cover = cover
        except:
            pass
        store.save()
        return redirect(reverse("store:detail", kwargs={"s_id": store.id}))


# 确认订单
def confirm(request):
    # 记录一条信息
    a = request.META['REMOTE_ADDR']
    logger = logging.getLogger('require_django')
    logger.info(a + '确认订单页面')
    return render(request, 'store/confirm.html', {})


# 结算
def pay(request):
    # 记录一条信息
    a = request.META['REMOTE_ADDR']
    logger = logging.getLogger('require_django')
    logger.info(a + '结算页面')
    return render(request, 'store/pay.html', {})
