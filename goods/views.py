from django.shortcuts import render

# Create your views here.


# 商品购买
def product(request):
    return render(request, "goods/product.html", {})


# 商品添加
def add(request):
    if request.method == "GET":
        return render(request,"goods/add.html",{})