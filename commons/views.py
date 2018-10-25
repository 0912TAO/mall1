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
    # 手机类型
    shouji_type1 = GoodType.objects.filter(pk=10001)
    shouji_type2 = GoodType.objects.filter(parent=shouji_type1)
    shouji = Goods.objects.filter(goodstype__in=shouji_type2)

    # 家电类型
    jiadian_type1 = GoodType.objects.filter(pk=10002)
    jiadian_type2 = GoodType.objects.filter(parent=jiadian_type1)
    jiadian = Goods.objects.filter(goodstype__in=jiadian_type2)

    # 手机配件
    peijian_type1 = GoodType.objects.filter(pk=10003)
    peijian_type2 = GoodType.objects.filter(parent=peijian_type1)
    peijian = Goods.objects.filter(goodstype__in=peijian_type2)

    # 智能数码
    shuma_type1 = GoodType.objects.filter(pk=10004)
    shuma_type2 = GoodType.objects.filter(parent=shuma_type1)
    shuma = Goods.objects.filter(goodstype__in=shuma_type2)

    return render(request, "commons/index.html", {"store": s, "goods": goods, "shouji": shouji,
                                                  "jiadian": jiadian, "peijian": peijian, "shuma": shuma
                                                  })


# 验证码
def code(request):
    img, code = utils.create_code()
    # 首先需要将code 保存到session 中
    request.session['code'] = code
    # 返会图片
    file = BytesIO()
    img.save(file, 'PNG')

    return HttpResponse(file.getvalue(), "image/png")