"""
WSGI config for cbgears project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

import env
os.environ['COLLECTIVE_NAME'] = 'wsgi'
# os.environ['LOG_CONFIG'] = os.path.join(BASE_DIR, os.environ['CONF'], 'log.conf')


from django.conf import settings
from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application()
def application(environ, start_response):
    if sys.platform == 'win32':
        if settings.FORCE_SCRIPT_NAME:
            environ['PATH_INFO'] = environ['PATH_INFO'].replace(
                settings.FORCE_SCRIPT_NAME, '', 1)
    return _application(environ, start_response)
