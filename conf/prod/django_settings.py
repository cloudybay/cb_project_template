import os

# DATABASES = {
# }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(os.environ.get("BASE_DIR"), "cache"),
        'TIMEOUT': 30,
    }
}

DEBUG = False
COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False

APPEND_SLASH = False
ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

FORCE_SCRIPT_NAME = ""
STATIC_URL = FORCE_SCRIPT_NAME + '/static/'
MEDIA_URL = FORCE_SCRIPT_NAME + '/media/'

SESSION_COOKIE_SECURE = True

CSRF_USE_SESSIONS = True

X_FRAME_OPTIONS = 'DENY'
