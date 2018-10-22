from django.shortcuts import render
from django.shortcuts import HttpResponse

from io import BytesIO
from . import utils

# Create your views here.


# 主页
def index(request):
        return render(request, "commons/index.html", {})


# 验证码
def code(request):
    img, code = utils.create_code()
    # 首先需要将code 保存到session 中
    request.session['code'] = code
    # 返会图片
    file = BytesIO()
    img.save(file, 'PNG')

    return HttpResponse(file.getvalue(), "image/png")