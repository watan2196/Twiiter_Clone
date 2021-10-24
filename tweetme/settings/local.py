import os
from .base import PROJECT_ROOT

SECRET_KEY = ')_3sp#ux^9bas4!u*krx*m@f_wwf7*u^t1_ivsl@x$5sew0rp*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('TWEET_DB_NAME', 'tweet_clone'),
        'USER': os.environ.get('TWEET_DB_USER', 'root'),
        'PASSWORD': os.environ.get('TWEET_DB_PASSWORD', 'Watansahu2196@'),
        'HOST': os.environ.get('TWEET_DB_HOST', 'localhost'),
        'PORT': '3306'
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_ROOT), "static-serve")
