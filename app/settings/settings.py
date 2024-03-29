"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

from celery.schedules import crontab
from django.urls import reverse_lazy
from environ import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tjiwi$+_qta@5*n0g7-87il==lg+d$%&^o7+&pcj6*08zl+&3!'

# SECURITY WARNING: don't run with debug turned on in production!


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),  # если в .env DEBUG не задан, то он False
)

environ.Env.read_env(os.path.join(BASE_DIR.parent, '.env'))  # parent - на директорию выше (не в app .env, а в currency)

DEBUG = env('DEBUG')  # для задания True или False через файл .env

# DEBUG = True  # Truе - при режиме настройки, при размещении на сервере False. При True все ошибки видны пользователю.
# Если установлен False, то статика не подтягивается

# ALLOWED_HOSTS = ['*']  # при '*' любой может зайти. для входа только с этого компьютера вместо '*' - '127.0.0.1'
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', [])  # если ALLOWED_HOSTS' не задано, то никто войти не сможет - []

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXTERNAL_APPS = [
    'django_extensions',
    'debug_toolbar',
    'crispy_forms',
    'crispy_bootstrap4',
    'django_filters',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',   # генератор документации
]

INTERNAL_APPS = [
    'currency',
    'account'
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'currency.middlewares.RequestResponseTimeMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR/'templates'
        ],
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

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# использование базы данных sqlite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# использование базы данных Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB', 'currency-db'),
        'USER': env.str('POSTGRES_USER', ''),
        'PASSWORD': env.str('POSTGRES_PASSWORD', ''),
        'HOST': env.str('POSTGRES_HOST', 'localhost'),
        'PORT': env.str('POSTGRES_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # размещение статических файлов

# При DEBUG=True  необходимо всю статику собрать в одну дирректорию и выполнить команду python manage.py collectstatic
STATIC_ROOT = BASE_DIR.parent / 'static_content' / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR.parent / 'static_content' / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # для оправки email в консоли

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587   # Порт 25, 465 или 587.
# EMAIL_HOST_USER = '*************@gmail.com'
# EMAIL_HOST_PASSWORD = '************'


LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('login')

AUTH_USER_MODEL = 'account.User'

if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

HOST = 'localhost:8000'
HTTP_SCHEMA = 'http'

# CELERY

# REDIS_HOST = 'localhost'
# REDIS_PORT = '6379'

# CELERY_BROKER_URL = "redis://localhost:6379"

# при работе без файла ,env
# CELERY_BROKER_URL = 'amqp://localhost'

# при работе с файлом .env
CELERY_BROKER_URL = 'amqp://{0}:{1}@{2}:{3}//'.format(
    env.str('RABBITMQ_DEFAULT_USER', 'guest'),
    env.str('RABBITMQ_DEFAULT_PASS', 'guest'),
    env.str('RABBITMQ_DEFAULT_HOST', '127.0.0.1'),
    env.str('RABBITMQ_DEFAULT_PORT', '5672')
)

# '''
# протокол общения с брокером:  amqp,
# месторасположения сервера:    localhost,
# порт по умолчанию:            5672,
# логин, пароль:                guest, guest
# '''

# планировщик задач
CELERY_BEAT_SCHEDULE = {
    'monobank': {
        'task': 'currency.tasks.parse_privatbank',      # задача к выполнению def parse_monobank
        'schedule': crontab(minute='*/15')               # каждые 15 минут
    },
    'privatbank': {
        'task': 'currency.tasks.parse_monobank',
        'schedule': crontab(minute='*/15')
    },
    'creditdneprbank': {
        'task': 'currency.tasks.parse_creditdneprbank',
        'schedule': crontab(minute='*/15')
    }
}

# Для работы с кэшированием Memcached
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
#         "LOCATION": "127.0.0.1:11211",  # при выгрузке на внешнем сервере параметры изменить
#     }
# }

# Для работы через образ
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": f"{env.str('CACHE_DEFAULT_HOST', '127.0.0.1')}:{env.str('CACHE_DEFAULT_PORT', '127.0.0.1')}",
    }
}

#  Авторизация через API с помощью токенов
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # 401
    ),
    'DEFAULT_PERMISSION_CLASSES': (    # если закомитить, то вход без авторизации через api по токенам
        'rest_framework.permissions.IsAuthenticated',  # 403
    ),
    'DEFAULT_THROTTLE_RATES': {    # ограничение по количеству запросов пользователем
        'currency': '20/min',       # класс прописан в throttlers.py и укзана в views только для RateViewSet
    },
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',  # настройка для Pytests, т.е. в запросах будут только json
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=14),  # период дейстивя Access token
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # период дейстивя Refresh token
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',      # алгоритм шифрования
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer', 'JWT',),   # название в запросе перед Refresh token
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Для хранения данных в облаке
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # для django-storages
# AWS_ACCESS_KEY = ''
# AWS_SECRET_ACCESS_KEY = ''
# AWS_STORAGE_BUCKET_NAME = 'hillel-sheketa'
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_REGION_NAME = 'eu-central-1'
# MEDIA_URL = 'https://hillel-sheketa.s3.eu-central-1.amazonaws.com/media/'
# AWS_DEFULT_ACL = 'public-read'
