# -*- coding: utf-8 -*-
from .settings import *

DEBUG = False
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

ALLOWED_HOSTS = ['*']

# FORCE_SCRIPT_NAME = ''
# STATIC_URL = FORCE_SCRIPT_NAME + '/static/'
# MEDIA_URL = FORCE_SCRIPT_NAME + '/media/'

# CONF_DIR = "prod"

from .database import GET_DATABASES
DATABASES = GET_DATABASES({})

from django.utils.crypto import get_random_string
SECRET_KEY = get_random_string(50, SECRET_KEY)
