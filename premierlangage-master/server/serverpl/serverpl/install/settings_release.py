"""
Django settings for serverpl project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os, sys
from datetime import date
from django.contrib.messages import constants as messages

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "o!m$n&s4=kcftm1de1m+7!36a=8x38wrr)m9)i@ru7j-*c7vgm"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'pl-test.u-pem.fr', 'pl.u-pem.fr']

# Used by mail_admins log handler, set ENABLE_MAIL_ADMINS to True to use it (DEBUG should also be set to False)
ENABLE_MAIL_ADMINS = True
MAIL_HOST = ''
MAIL_PORT = 25
ADMINS = [
    #('Coumes Quentin',      'qcoumes@etud.u-pem.fr'),
    #('Revuz Dominique',     'Dominique.Revuz@u-pem.fr'),
    #('Cuvelier Nicolas',    'ncuvelie@etud.u-pem.fr'),
]

# Application definition
INSTALLED_APPS = [
    'gitload',
    'playexo',
    'classmanagement',
    'sandbox',
    'documentation',
    'markdown_deux',
    'bootstrap3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_auth_lti',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_auth_lti.middleware_patched.MultiLTILaunchAuthMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 5*365*24*60*60

LOGIN_URL = "/playexo/not_authenticated/"

ROOT_URLCONF = 'serverpl.urls'

#Overriding "messages.ERROR: 'error'" to danger to correspond to the bootstrap alert tag
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
        ],
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
        
    },

]

WSGI_APPLICATION = 'serverpl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

#Write email in console instead of sending it if mailing is disable or DEBUG is set to True
if DEBUG or not ENABLE_MAIL_ADMINS:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#Logger information
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)-15s] %(levelname)s -- File: %(pathname)s line n°%(lineno)d -- %(message)s',
            'datefmt': '%Y/%m/%d %H:%M:%S'
        },
        'simple': {
            'format': '[%(asctime)-15s] %(levelname)s -- %(message)s',
            'datefmt': '%Y/%m/%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'facility': 'local7',
            'address': '/dev/log',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django':{
            'handlers': ['console', 'syslog', 'mail_admins'],
            'level': 'INFO',
        },
        'sandbox':{
            'handlers': ['console', 'syslog', 'mail_admins'],
            'level': 'INFO',
        },
        'classmanagement':{
            'handlers': ['console', 'syslog', 'mail_admins'],
            'level': 'INFO',
        },
        'documentation':{
            'handlers': ['console', 'syslog', 'mail_admins'],
            'level': 'INFO',
        },
        'gitload':{
            'handlers': ['console', 'syslog', 'mail_admins'],
            'level': 'INFO',
        },
        'playexo':{
            'handlers': ['console', 'syslog', 'mail_admins'],
            'level': 'INFO',
        },
        'pysrc':{
            'handlers': ['console', 'syslog', 'mail_admins'],
            'level': 'INFO',
        },
        'django_auth_lti':{
            'handlers': ['console', 'syslog', 'mail_admins'],
            'level': 'INFO',
        },
    },
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_auth_lti.backends.LTIAuthBackend',
)

LTI_OAUTH_CREDENTIALS = {
    'moodle': 'secret',
    'test2': 'moodle'
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = False

USE_L10N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles')
STATIC_URL = '/static/'


MEDIA_ROOT = os.path.join(PROJECT_DIR, '../../../../tmp')
MEDIA_URL = '/tmp/'

REPO_ROOT = os.path.join(PROJECT_DIR,'../../../repo')

# python plank packtage dir  
PYSRCDIR = os.path.dirname(PROJECT_DIR + "/../pysrc/")
if not PYSRCDIR in sys.path:
    sys.path.append(PYSRCDIR)

DIRREPO = REPO_ROOT # TODO: replace every occurence of DIRREPO with REPO_ROOT