# -*- coding: utf-8 -*-
"""
This using for testing environment
"""

from settings import *


DEBUG = True

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ["127.0.0.1"]
INTERNAL_IPS = tuple(INTERNAL_IPS)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'frims-features',
        'TIMEOUT': 1,
    }
}


DB_PARAMS = {
    'HOST': '192.168.1.103',
    'USER': 'cb',
    'PASSWORD': 'cb2009',
}


PREFIX_URL = '/{{ project_name }}'

STATIC_URL = PREFIX_URL + '/static/'

MEDIA_URL = PREFIX_URL + '/media/'

