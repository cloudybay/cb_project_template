# -*- coding: utf-8 -*-
"""
This using for operation environment
"""

from settings import *


DEBUG = False

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ["127.0.0.1"]
INTERNAL_IPS = tuple(INTERNAL_IPS)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR + "/cache",
        'TIMEOUT': 600,
    }
}


DB_PARAMS = {
    'HOST': 'localhost',
    #'USER': '',
    #'PASSWORD': '',
}


PREFIX_URL = '/{{ project_name }}'

STATIC_URL = PREFIX_URL + '/static/'

MEDIA_URL = PREFIX_URL + '/media/'

