from django.shortcuts import render

# Create your views here.


# 我的购物车
def my_cart(request):
    # GET方式打开页面
    if request.method == 'GET':
        return render(request, 'store/my_cart.html', {})

    # POST方式打开页面
    elif request.method == 'POST':
        pass


# 开店
def open_shop(request):
    if request.method == 'GET':
        return render(request, 'store/open_shop.html', {})
    else:
        pass


# 确认订单
def confirm(request):
    return render(request, 'store/confirm.html', {})


# 结算
def pay(request):
    return render(request, 'store/pay.html', {})