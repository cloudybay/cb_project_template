import os
import sys
import django
from channels.routing import get_default_application

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

import env

django.setup()
from django.conf import settings
application = get_default_application()

ROOT_PATH = settings.FORCE_SCRIPT_NAME
from uvicorn.workers import UvicornWorker
class DjangoUvicornWorker(UvicornWorker):
    """
    A worker class for Gunicorn that interfaces with an ASGI consumer callable,
    rather than a WSGI callable.
    """

    CONFIG_KWARGS = {"loop": "uvloop", "http": "httptools", "root_path": ROOT_PATH}
