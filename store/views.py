from django.shortcuts import render,reverse,redirect
from django.contrib.auth.decorators import login_required   # 需要登陆的装饰器
from django.shortcuts import render,redirect,reverse
from django.views.decorators.http import require_GET
from . import models
import logging

from goods.models import GoodType, Goods
from shopcat.models import ShopCart
from . import models


# 添加到购物车
@login_required
def add(request, goods_id):
    # 商品ID
    goods = Goods.objects.get(pk=goods_id)
    print(goods.price)
    user = request.user
    shopCart = ShopCart.objects.filter(user=user, goods=goods)
    # print('***************')
    # print('shopcart',shopCart)
    # print('***************')
    # 查购物车
    try:
        # 如果有购物车
        shopCart = ShopCart.objects.get(user=user, goods=goods)

        # 更新数量
        shopCart.count += 1

        # 小计金额 = 数量 * 单价
        shopCart.allTotal = goods.price * shopCart.count
        # 保存
        shopCart.save()
    except:
        # 如果没有购物车 添加购物车
        shopCart = ShopCart(goods=goods, user=user)
        # shopCart.count = int(count)

        # 小计金额 = 数量 * 单价
        shopCart.allTotal = goods.price

        shopCart.save()

    return redirect(reverse('store:add_true'))


# 我的购物车
@login_required
@require_GET
def my_cart(request):
    # GET方式打开页面
    if request.method == 'GET':
        # 记录一条信息
        a = request.META['REMOTE_ADDR']
        logger = logging.getLogger('require_django')
        logger.info(a + '打开购物车')

        # 查询自己的商品
        shopcarts = ShopCart.objects.filter(user=request.user)
        # print(shopcarts)
        return render(request, 'store/my_cart.html', {'shopcarts': shopcarts})

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
@login_required
def delete(request, s_id):
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
@login_required
def confirm(request):
    # 记录一条信息
    a = request.META['REMOTE_ADDR']
    logger = logging.getLogger('require_django')
    logger.info(a + '确认订单页面')

    # # 获取选择的多个数据 列表
    # g_ids = request.POST.getlist('g_id')
    # # 查询多个商品
    # goods = ShopCart.goods.objects.filter(pk__in=g_ids)
    #
    # # 生成订单
    # for g in goods:
    #     models.OrderItem(good_id=g.id, goods_name=g.name,)


    return render(request, 'store/confirm.html', {})


# 结算
@login_required
def pay(request):
    # 记录一条信息
    a = request.META['REMOTE_ADDR']
    logger = logging.getLogger('require_django')
    logger.info(a + '结算页面')
    return render(request, 'store/pay.html', {})


# 宝贝
@login_required
def baobei(request, s_id):
    store = models.store.objects.get(pk=s_id)
    type1 = GoodType.objects.filter(parent__isnull=True)
    goods = Goods.objects.filter(stores=store)
    return render(request, "store/baobei.html", {"store": store, "type1": type1, "goods": goods})
    # return render(request, "store/baobei.html", {})


# 添加成功
def add_true(request):
    return render(request, 'store/add_true.html', {})


# 删除商品
@login_required
def delete(request, s_id):
    at = ShopCart.objects.get(pk=s_id)
    at.delete()
    return redirect(reverse("store:my_cart"))