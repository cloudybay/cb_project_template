# -*- coding: utf-8 -*-
from .settings import *

DEBUG = True
COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ["127.0.0.1"]
INTERNAL_IPS.extend(["192.168.1.%d"%ip for ip in range(120, 241)])
INTERNAL_IPS = tuple(INTERNAL_IPS)

# FORCE_SCRIPT_NAME = ''
# STATIC_URL = FORCE_SCRIPT_NAME + '/static/'
# MEDIA_URL = FORCE_SCRIPT_NAME + '/media/'

from .database import GET_DATABASES
DATABASES = GET_DATABASES({})
