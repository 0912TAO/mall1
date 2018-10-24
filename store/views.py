<<<<<<< HEAD
from django.shortcuts import render,reverse,redirect
from django.contrib.auth.decorators import login_required   # 需要登陆的装饰器
from . import models
=======
from django.shortcuts import render,redirect,reverse

>>>>>>> ca8defcd1c61002d02d2df97188c5d02789def04
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


<<<<<<< HEAD
@login_required
=======
# 开店
>>>>>>> ca8defcd1c61002d02d2df97188c5d02789def04
def open_shop(request):
    store = models.store.objects.filter(user_id=request.user.id)
    print(store)

    return render(request, 'store/open_shop.html', {"store": store})


@login_required
def i_want_open_shop(request):
    if request.method == 'GET':
<<<<<<< HEAD
        return render(request, 'store/i_want_open_shop.html', {})
    if request.method == 'POST':
        name = request.POST['name']
        intro = request.POST['intro']
        try:
            cover = request.FILES['cover']
            store = models.store(name=name, intro=intro, cover=cover, user=request.user)

        except:
            store = models.store(name=name, intro=intro, user=request.user)
        store.save()
        # 跳转有问题
        return redirect(reverse("store:open_shop", kwargs={"store": store}))
=======
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

# 确认订单
def confirm(request):
    return render(request, 'store/confirm.html', {})


# 结算
def pay(request):
    return render(request, 'store/pay.html', {})
<<<<<<< HEAD

=======
>>>>>>> bad801507888049a45a0e9f338bc8fb8cda42e39
>>>>>>> ca8defcd1c61002d02d2df97188c5d02789def04
>>>>>>> 3b102c1f87cde6f2b626b5c8b867bd8c54d52147
