from django.shortcuts import render,reverse,redirect
from django.contrib.auth.decorators import login_required   # 需要登陆的装饰器
from . import models
# Create your views here.


# 我的购物车
def my_cart(request):
    # GET方式打开页面
    if request.method == 'GET':
        return render(request, 'store/my_cart.html', {})

    # POST方式打开页面
    elif request.method == 'POST':
        pass


@login_required
def open_shop(request):
    store = models.store.objects.filter(user_id=request.user.id)
    print(store)

    return render(request, 'store/open_shop.html', {"store": store})


@login_required
def i_want_open_shop(request):
    if request.method == 'GET':
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
