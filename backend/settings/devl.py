import os

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i+acxn5(akgsn!sr4^qgf(^m&*@+g1@u^t@=8s@axc41ml*f=s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': '',
        'NAME': 'testdb',
    }
}

INTERNAL_IPS = ['192.168.56.1']

INSTALLED_APPS += (
    'autofixture',
)


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, '../../staticfiles')
STATIC_URL = '/staticfiles/'



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_DIRS.append(
    os.path.join(BASE_DIR, '../frontend', 'build'),
)


