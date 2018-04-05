"""
Django settings for liedfestival project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import json

###########################
DEBUG = True
###########################


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(BASE_DIR + "/.mysettings", "r") as j:
    mysettings = json.load(j)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if 'SECRET_KEY' in mysettings:
    SECRET_KEY = mysettings['SECRET_KEY']


if 'EMAIL_BACKEND' in mysettings:
    EMAIL_BACKEND = mysettings['EMAIL_BACKEND']

###

if 'EMAIL_HOST' in mysettings:
    EMAIL_HOST = mysettings['EMAIL_HOST']

if 'EMAIL_HOST_USER' in mysettings:
    EMAIL_HOST_USER = mysettings['EMAIL_HOST_USER']

if 'EMAIL_HOST_PASSWORD' in mysettings:
    EMAIL_HOST_PASSWORD = mysettings['EMAIL_HOST_PASSWORD']

if 'EMAIL_PORT' in mysettings:
    EMAIL_POST = mysettings['EMAIL_PORT']

if 'EMAIL_USE_TLS' in mysettings:
    EMAIL_USE_TLS = mysettings['EMAIL_USE_TLS']

####

if "MAILJET_API_KEY" in mysettings:
    MAILJET_API_KEY = mysettings['MAILJET_API_KEY']

if "MAILJET_API_SECRET" in mysettings:
    MAILJET_API_SECRET = mysettings['MAILJET_API_SECRET']

####

ALLOWED_HOSTS = ['liedfestivalkassel.pythonanywhere.com', 'localhost', '192.168.2.108']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
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

ROOT_URLCONF = 'liedfestival.urls'

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

WSGI_APPLICATION = 'liedfestival.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DB_PREFIX = 'DB_LOCAL_'

if mysettings['ENVIRONMENT']:
    DB_PREFIX = 'DB_' + mysettings['ENVIRONMENT'].upper() + '_'

DATABASES = {
    'default': {
        'ENGINE': mysettings[DB_PREFIX + 'ENGINE'],
        'HOST': mysettings[DB_PREFIX + 'HOST'],
        'NAME': mysettings[DB_PREFIX + 'NAME'],
        'USER': mysettings[DB_PREFIX + 'USER'],
        'PASSWORD': mysettings[DB_PREFIX + 'PASSWORD'],
    },
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Media root

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'home/static/media')
