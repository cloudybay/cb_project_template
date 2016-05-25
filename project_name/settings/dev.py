# -*- coding: utf-8 -*-
"""
This using for development
"""

from settings import *


DEBUG = True

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ["127.0.0.1"]
INTERNAL_IPS.extend(["192.168.1.%d"%ip for ip in range(120, 241)])
INTERNAL_IPS = tuple(INTERNAL_IPS)


DB_PARAMS = {
    'HOST': '192.168.1.103',
    'USER': 'cb',
    'PASSWORD': 'cb2009',
}


PREFIX_URL = ''

STATIC_URL = PREFIX_URL + '/static/'

MEDIA_URL = PREFIX_URL + '/media/'

