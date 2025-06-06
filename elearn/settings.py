"""
Django settings for elearn project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u)q%w7rq)(_%pzir6ladr)v46xd0x$!0(3!4mr^^kcqcj$sor('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt', 
    'authentication',
    'courses',
    'channels',
    'chat',  # Add your chat app
]  


    


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'elearn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             os.path.join(BASE_DIR, 'templates'),
             os.path.join(BASE_DIR, 'frontend/templates'),
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

WSGI_APPLICATION = 'elearn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'elearning',        
        'USER': 'postgres',       
        'PASSWORD': '1234567890',  
        'HOST': 'localhost',       
        'PORT': '5432',         
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'authentication.CustomUser'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),
}
AUTHENTICATION_BACKENDS = (
   'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
    # 'social_core.backends.google.GoogleOAuth2',
    # 
     )

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "elearning198@gmail.com"
EMAIL_HOST_PASSWORD = "iraj ulpz qobv yvck"
DEFAULT_FROM_EMAIL = "Telead <elearning198@gmail.com>"

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

SITE_ID = 1

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STRIPE_SECRET_KEY = "sk_test_51Q3cprGdR9qlor6Wu8EbW6c3q0EPwxG6uZexluIJ0L1gpIb8yctQ2hKWKF9ZoaeeTxjPrF0TQXBUfFchhQQ5PqOF001OVWR7Hf"
STRIPE_PUBLIC_KEY = "pk_test_51Q3cprGdR9qlor6WgE2wWf7ifRCARjGMQw4COUbeSejSrBQKK00vzHItg6MMmK47w7XFTCXKPbiOG1fuP03tzyrA002CiBNOTK"
STRIPE_WEBHOOK_SECRET = "whsec_2f0a345c76648c3f61aeb6830431a7201f4ac1aa04514796d7d3c374df879e20"

ASGI_APPLICATION = 'elearn.asgi.application'

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('127.0.0.1', 6379)],
#         },
#     },
# }
# 'channels.layers.InMemoryChannelLayer'

# settings.py

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

