from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required   # 需要登陆的装饰器
from django.shortcuts import render,redirect,reverse
from django.views.decorators.http import require_GET
from . import models
import logging

from goods.models import GoodType, Goods
from user.models import Address,User
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
        return render(request, 'store/open_shop.html', {})
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
        return redirect(reverse("store:open_shop", kwargs={"s_id":store1.id}))


# 商铺列表
# @require_GET
# @login_required()
# def list(request):
#     stores = models.store.objects.filter(user=request.user,status__in =[0,1])
#     return render(request,"store/list.html",{"stores":stores})


# 细节（店铺详情）
# @require_GET
# @login_required()
# def detail(request,s_id):
#     store = models.store.objects.get(pk=s_id)
#     type1 = GoodType.objects.filter(parent__isnull=True)
#     goods = Goods.objects.filter(stores=store)
#     return render(request,"store/detail.html",{"store":store,"type1":type1,"goods":goods})


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
def update(request, s_id):

    if request.method == "GET":
        store = models.store.objects.get(pk=s_id)
        print(store.name)
        return render(request, "store/goodsupdate.html", {"store": store})
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


# 添加地址
@login_required()
def address(request):
    if request.method =="GET":
        return render(request, 'store/address.html', {})
    else:
        # 收货人
        recr_name = request.POST["recr_name"]
        # 收货人电话
        recr_tel = request.POST["recr_tel"]
        # 收货人所在省份
        province = request.POST["province"]
        # 收货人所在城市
        city = request.POST["city"]
        # 收货人所在县区
        area = request.POST["area"]
        # 收货人详细地址
        street = request.POST["street"]
        # 邮政编码
        postal = request.POST["postal"]
        # 地址标签
        add_label = request.POST["add_label"]
        try:
            # 默认地址
            is_default = request.POST["is_default"]
            addresses = Address.objects.filter(user=request.user)
            for address in addresses:
                address.is_default = False
                address.save()
            address = Address(recr_name=recr_name, recr_tel=recr_tel, province=province, city=city, area=area,street=street,postal=postal,add_label=add_label,user=request.user,is_default=True)
            address.save()
        except:
            address = Address(recr_name=recr_name, recr_tel=recr_tel, province=province, city=city, area=area,
                              street=street, postal=postal, add_label=add_label, user=request.user)
            address.save()
        return redirect(reverse("store:confirm"))


def address_list(request):
    addresses = Address.objects.filter(user=request.user)

    return render(request,"store/address_list.html",{"addresses":addresses})



# 确认订单
@login_required
def confirm(request):

    # 记录一条信息
    a = request.META['REMOTE_ADDR']
    logger = logging.getLogger('require_django')
    logger.info(a + '确认订单页面')

    # 获取购物车中选择的多个商品数据 列表
    g_ids = request.POST.getlist('g_id')
    # 查询购物车商品
    shopCarts = ShopCart.objects.filter(user=request.user)

    # 根据商品查询多个商品 对象
    # goods = my_shop_cart.goods.objects.filter(pk__in=g_ids)

    # 查询客户地址
    addresses = Address.objects.filter(user=request.user)

<<<<<<< HEAD
    return render(request, 'store/confirm.html', {})
=======
    print("*******************")
    print(shopCarts)
    print(addresses)
    print("*******************")

    return render(request, 'store/confirm.html', {'shopCarts': shopCarts, 'addresses': addresses})
>>>>>>> 338b44e8e63bad703f7ccf2bd1d8297c21a3d1e2


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


# 修改商品
def goodsupdate(request, g_id):
    type1 = GoodType.objects.filter(parent__isnull=True)
    s = Goods.objects.get(pk=g_id)
    print(s.name, s.id, s.stores_id)
    store = models.store.objects.get(pk=s.stores_id)
    if request.method == 'GET':
        return render(request, "store/goodsupdate.html", {"store": store, "s": s, "type1":type1})
    if request.method == 'POST':
        price = request.POST['price']
        stock = request.POST['stock']
        type2 = request.POST["type2"]

        goodsType = GoodType.objects.get(pk=type2)
        # 保存商品
        g = Goods.objects.get(pk=g_id)
        g.price=price
        g.stock=stock
        g.goodstype=goodsType
        g.save()
        goods = Goods.objects.filter(stores=store)
        return render(request, "store/baobei.html", {"store": store, "type1": type1, "goods": goods})


# 永久删除商品
def goodsdel(request, g_id):
    s = Goods.objects.get(pk=g_id)
    store = models.store.objects.get(pk=s.stores_id)
    type1 = GoodType.objects.filter(parent__isnull=True)
    goods = Goods.objects.filter(stores=store)
    g = Goods.objects.get(pk=g_id)
    g.delete()
    return render(request, "store/baobei.html", {"store": store, "type1": type1, "goods": goods})