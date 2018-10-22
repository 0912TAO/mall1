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


def open_shop(request):
    if request.method == 'GET':
        return render(request, 'store/open_shop.html', {})
    else:
        pass