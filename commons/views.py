from django.shortcuts import render
from django.shortcuts import HttpResponse

from io import BytesIO
from . import utils
from store import models

# Create your views here.


# 主页
def index(request):
    store = models.store.objects.filter(user_id=request.user.id)
    return render(request, "commons/index.html", {"store":store})


# 验证码
def code(request):
    img, code = utils.create_code()
    # 首先需要将code 保存到session 中
    request.session['code'] = code
    # 返会图片
    file = BytesIO()
    img.save(file, 'PNG')

    return HttpResponse(file.getvalue(), "image/png")