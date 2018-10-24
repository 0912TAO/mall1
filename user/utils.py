from mall import settings
from django.core.mail import send_mail




# def number():
#
#     num = random.randint(1000, 9999)
#     return num
#
# print(number())


def login_email(emil1):
    title = '没有中间商赚差价'
    content = '您的激活码是 “6666” '
    # content = number()

    send_obj_list = emil1
    # sj = js()
    send_html_message = "邮箱验证码"
    sem_start = send_mail(title, content, settings.EMAIL_FROM, [send_obj_list], send_html_message)
    print("邮箱已发送")
    if sem_start:
        pass