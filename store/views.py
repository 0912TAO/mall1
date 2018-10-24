from django.shortcuts import render,redirect,reverse

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET

from . import models


# 我的购物车
def my_cart(request):
    # GET方式打开页面
    if request.method == 'GET':
        return render(request, 'store/my_cart.html', {})

    # POST方式打开页面
    elif request.method == 'POST':
        pass


def open_shop(request):
    if request.method == 'GET':
        return render(request, 'store/open_shop.html', {})
    else:
        pass


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
@require_GET
@login_required()
def list(request):
    stores = models.store.objects.filter(user=request.user,status__in =[0,1])
    return render(request,"store/list.html",{"stores":stores})


# 细节（店铺详情）
@require_GET
@login_required()
def detail(request,s_id):
    store = models.store.objects.get(pk=s_id)
    return render(request,"store/detail.html",{"store":store})


# 店铺状态更改
@login_required()
def change(request,s_id,status):
    store = models.store.objects.get(id=s_id)
    store.status = int(status)
    store.save()
    if store.status == 2:
        return redirect(reverse("store:list"))
    else:
        return render(request, "store/detail.html", {"store": store})


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