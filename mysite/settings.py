"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from configurations import Configuration

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Base(Configuration):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '(ys(b=s=^5(u$hl8^))h_h3j^r*mg+t#vw%7c*zb6z-&hq-=8-'

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
    )

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
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

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'America/Tijuana'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    ALLOWED_HOSTS = [
        '127.0.0.1',
        '0.0.0.0'
    ]

    MIDDLEWARE_CLASSES = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    ]

    MIDDLEWARE = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ]

    WSGI_APPLICATION = 'mysite.wsgi.application'

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    LOGIN_REDIRECT_URL = '/'

    STATIC_URL = '/static/'

    ROOT_URLCONF = 'mysite.urls'


class Dev(Base):
    DEBUG = True

    MIDDLEWARE = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware'
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    ALLOWED_HOSTS = [
        '127.0.0.1'
    ]


class Prod(Base):
    DEBUG = False

    DATABASES = {'default': dj_database_url.config(conn_max_age=500)}

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    ALLOWED_HOSTS = [
        'elifloresch.pythonanywhere.com',
        'mignonnesaurus.herokuapp.com'
    ]
