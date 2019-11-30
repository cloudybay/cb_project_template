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
ALLOWED_HOSTS = []

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# FORCE_SCRIPT_NAME = ""
