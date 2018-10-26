from django.shortcuts import render
from django.shortcuts import redirect   # 路由重定向
from django.shortcuts import HttpResponse
from django.core.urlresolvers import reverse    # 反解析
from django.http import JsonResponse
from django.db import transaction   # django 事物
from django.contrib.auth import authenticate, login, logout     # 内置的用户认证
from django.contrib.auth.decorators import login_required   # 需要登陆的装饰器
from django.contrib.auth.models import User     # 引入django的User表

from .utils import login_email


from io import BytesIO  # 在内存中读写bytes
from commons import utils     # 工具模块

from . import models    # 模型模块
# Create your views here.


# 登录
def user_login(request):
    # GET方式打开页面
    if request.method == 'GET':
        try:
            next_url = request.GET['next']
        except:
            next_url = "/commons/index/"

        print(next_url)
        return render(request, 'user/user_login.html', {"next_url": next_url})

    # POST方式打开页面
    elif request.method == 'POST':
        # 点击登录post传值
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST.get("next", "/commons/index/")
        islong = request.POST.get("islong", "no")
        # print(is_long)
        # return
        print(next_url)

        # 验证账号密码
        user = authenticate(username=username, password=password)
        # session
        request.session["loginUser"] = user
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session["LoginUser"] = user
                if islong == "on":
                    request.session.set_expiry(3600 * 24 * 7)
                elif islong == "no":
                    request.session.set_expiry(0)
                return redirect(next_url)
                # return render(request, 'user/index.html', {"user": user})
            else:
                return render(request, 'user/user_login.html', {"msg": "您的账号已被禁用，请联系管理员"})
        else:
            return render(request, 'user/user_login.html', {"msg": "账号或密码错误，请重新登录"})


# 注册
@transaction.atomic
def register(request):
    # GET方式打开页面
    if request.method == "GET":
        return render(request, 'user/register.html', {})

    # 点击from提交之后
    elif request.method == "POST":
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        querenpassword = request.POST['querenpassword'].strip()
        code = request.POST['code']
        print(username, password, code)

        # 后台验证
        if code.upper() != request.session['code'].upper():
            return render(request, 'user/register.html', {"msg": "验证码不正确，请重新注册"})
        if len(password) < 6:
            return render(request, 'user/register.html', {"msg": "密码长度不足6位，请重新注册"})
        if password != querenpassword:
            return render(request, 'user/register.html', {"msg": "两次输入密码不一致，请重新注册"})

        try:
            # 用户名验证
            hyd = transaction.savepoint()
            User.objects.get(username=username)
            return render(request, 'user/register.html', {"msg": "用户名已存在，请重新注册"})
        except:
            try:
                # create_user辅助函数创建用户
                user = User.objects.create_user(username=username, password=password)
                usera = models.UserA(user=user)
                user.save()
                usera.save()
                # 事物
                transaction.savepoint_commit(hyd)
                # session
                request.session["loginUser"] = user
                return render(request, "user/tiaozhuan.html", {"msg": "恭喜注册成功，请登录"})
            except:
                # 事物
                transaction.savepoint_rollback(hyd)
                return render(request, "user/register.html", {"msg": "注册失败，请重新注册"})


def tiaozhuan(request):
    return render(request, "user/tiaozhuan.html", {{"msg": "恭喜注册成功，请登录"}})


# 个人中心
@login_required
def personal(request):
    userA = models.UserA.objects.get(user_id=request.user.id)
    if request.method == 'GET':
        return render(request, "user/personal.html", {"userA": userA})
    if request.method == 'POST':
        pass


# 修改个人信息
def changeinfo(request):
    userA = models.UserA.objects.get(user_id = request.user.id)
    if request.method == "GET":
        return render(request, "user/changeinfo.html", {"userA": userA})
    else:
        gender = request.POST.get('gender', 0)
        age = request.POST.get('age', 1)
        phone = request.POST.get('phone', "")
        add = request.POST.get('add', "")
        print(gender,age,phone,add)

        userA.gender = gender
        userA.age = age
        userA.phone = phone
        userA.add = add
        userA.save()
        return render(request, "user/changeinfo.html", {"userA": userA,"msg": "修改个人信息成功"})

# 修改用户头像
@login_required
def changeheader(request):
    userA = models.UserA.objects.get(user=request.user.id)
    if request.method == "GET":
        print(request.user.id)
        print("********")
        print(userA)
        print("-----------")
        return render(request, "user/changeheader.html", {"userA": userA})
    elif request.method == "POST":
        header = request.FILES.get("header", "static/image/default.jpg")
        print(header)
        print("获取到头像数据")
        userA.header = header
        userA.save()
        return render(request, "user/changeinfo.html", {"msg": "头像修改成功", "userA":userA})

# ajax验证旧密码
def check_password(request, old_password):
    u = User.objects.get(pk=request.user.id)
    print(u)
    print(u.username)
    user = authenticate(username=u.username, password=old_password)
    if user is None:
        return JsonResponse({"msg": "输入的旧密码不正确", "success": False})
    else:
        return JsonResponse({"msg": "正确", "success": True})


# 修改用户密码
@login_required
def changepwd(request):
    u = User.objects.get(pk=request.user.id)
    userA = models.UserA.objects.get(user_id=request.user.id)
    print(userA)
    if request.method == "GET":
        return render(request, "user/changepwd.html", {"userA": userA})
    if request.method == "POST":
        old_password = request.POST['old_password']
        password = request.POST['password']
        two_password = request.POST['two_password']

        print(old_password, password, two_password)

        user = authenticate(username=u.username, password=old_password)

        if user is None:
            return JsonResponse({"msg": "输入的旧密码不正确", "success": False})
        if len(password) < 6:
            return JsonResponse({"msg": "输入的新密码小于6位", "success": False})
        if password != two_password:
            return JsonResponse({"msg": "两次输入密码不一致", "success": False})

        try:
            # user = User.objects.create_user(username=u.username, password=password)
            # user.save()
            u.set_password(password)
            u.save()
            return JsonResponse({"msg": "修改密码成功", "success": True})
        except:
            return JsonResponse({"msg": "修改密码失败", "success": False})


# ajax验证用户名是否存在
def checkusername(requess ,uname):
    try:
        User.objects.get(username=uname)
        return JsonResponse({"msg": "用户名已存在，请重新输入", "success": False})
    except:
        return JsonResponse({"msg": "请继续输入", "success": True})


# 退出登录
# @login_required
def user_logout(request):
    logout(request)
    return render(request, 'user/user_logout.html', {"msg": "您已成功退出！"})


# ajax检测验证码
def checkcode(request, yzm):
    my_code = request.session['code']
    print(my_code)
    if yzm.upper() != my_code.upper():
        return JsonResponse({"msg": "验证码错误，请重新输入","success":False})
    else:
        return JsonResponse({"msg":"验证码正确", "success":True})


# 验证码
def code(request):
    img, code = utils.create_code()
    # 首先需要将code 保存到session 中
    request.session['code'] = code
    # 返会图片
    file = BytesIO()
    img.save(file, 'PNG')

    return HttpResponse(file.getvalue(), "image/png")


# 绑定邮箱
def email(request):
    return render(request, "user/email.html", {})


def save_email(request):
    u = User.objects.get(id=request.user.id)
    userA = models.UserA.objects.get(user_id=request.user.id)
    email = request.POST['email']
    code = int(request.POST['ma'])
    if code == 6666:
        u.email = email
        u.save()
        # return render(request, "user/personal.html", {"userA": userA})

        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})





# 发送邮件
def start_send_email(request):
    try:
        email1 = request.POST["email"]
        print("你的邮箱"+email1)
        login_email(email1)
        return HttpResponse()
    except Exception as e:
        print(e)
        return render(request, "user/reg_test.html",{})


# 邮箱登录
# def reg_login(request):
#     ma = request.POST['ma']
#     if ma == 6666:
#         try:
#             email = request.POST['email']
#             print("你的邮箱"+email)
#         except Exception as e:
#             pass


# 服务
def server(request):
    return render(request, "user/services.html", {})