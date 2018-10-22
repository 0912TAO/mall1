from django.shortcuts import render

# Create your views here.


# 商品购买
def product(request):
    return render(request, "goods/product.html", {})