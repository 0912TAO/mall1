from django.shortcuts import render
from django.shortcuts import HttpResponse

from io import BytesIO
from . import utils
from store.models import store
from goods.models import Goods
from goods.models import GoodsImage
from goods.models import GoodType
# Create your views here.


# 主页
def index(request):
    s = store.objects.filter(user_id=request.user.id)
    goods = GoodType.objects.filter(parent__isnull=True)
    shangpin = Goods.objects.all()
    print("******************")
    print(s)
    print(goods)
    print(shangpin)
    print("******************")
    # tupian = GoodsImage.objects.get(pk=shangpin)
    return render(request, "commons/index.html", {"store": s, "goods": goods, "shangpin":shangpin})


# 验证码
def code(request):
    img, code = utils.create_code()
    # 首先需要将code 保存到session 中
    request.session['code'] = code
    # 返会图片
    file = BytesIO()
    img.save(file, 'PNG')

    return HttpResponse(file.getvalue(), "image/png")