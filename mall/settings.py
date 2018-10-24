"""
Django settings for mall project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import pymysql  # 引入PyMysql

pymysql.install_as_MySQLdb()    # 转换数据库支持

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u(v)u41ff085z1kn97%k@xjp(@otu_8jrpjdyx^r-4$n74j38o'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'commons',  # 公共
    'goods',    # 产品
    'store',    # 商店
    'user',     # 用户
    # 'xadmin',
    # 'crispy_forms',
    # 'reversion',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 根模块下的templates文件
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# MySql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shopping',
        'HOST': '192.168.13.14',
        'PORT': 3306,
        'USER': 'manbanzhen',
        'PASSWORD': '123456'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 静态资源
STATIC_URL = '/static/'

# 根模块下的静态资源
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 序列化session
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# 判断是否登录的装饰器
LOGIN_URL = "/user/user_login/"


# 邮箱验证
# 163 SMTP 配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25  # 端口号
# 发送邮件的邮箱
EMAIL_HOST_USER = 'tom_tao0912@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'meng0912'
# 收件人看到的发件人
EMAIL_FROM = 'tom_tao0912@163.com'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/log/log.log',
        },
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
        }

    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },

        'require_django': {
            'handlers': ['file'],
            'level': 'INFO',
            'maxBytes': 1024 * 1024 * 5,
            'propagate': True,
        },
    },
}
