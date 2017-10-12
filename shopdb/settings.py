"""
Django settings for shopdb project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from ext_settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#(r-v08e2resceo+p5a38g6cinbnev=)5&w1mxgz1_gec3xtx('

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False

#ALLOWED_HOSTS = ['176.9.99.15', 'kvitky.pp.ua']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'shop',
    'cart',
    'auth_user',
    'log',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shopdb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'auth_user', 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'shopdb.wsgi.application'




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

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')


CART_SESSION_ID = 'cart'

REGISTRATION_OPEN = True


ACCOUNT_ACTIVATION_DAYS = 1


USE_I18N = True



########################


#loggers
LOG_FILE = os.path.join(BASE_DIR, 'shop.log')

LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
	'verbose': {
	  'format': '%(levelname)s %(asctime)s %(module)s: %(message)s'
	  },
	  'simple': {
	    'format': '%(levelname)s: %(message)s'
	  },
   },
   'handlers': {
     'null': {
       'level': 'DEBUG',
       'class': 'logging.NullHandler',
     },
     'console': {
       'level': 'INFO',
       'class': 'logging.StreamHandler',
       'formatter': 'verbose',
     },
     'file': {
     'level': 'INFO',
     'class': 'logging.FileHandler',
     'filename': LOG_FILE,
     'formatter': 'verbose'
     },
     'database': {
            'level': 'DEBUG',
            'class': 'shopdb.custom_handlers.DatabaseHandler',
            'formatter': 'verbose'
     },
   },
   'loggers': {
     'django': {
       'handlers': ['null'],
       'propagate': True,
       'level': 'INFO',
     },
     'shop.signals': {
     'handlers': ['file','console', 'database'],
     'level': 'INFO',
     }

   }
}
