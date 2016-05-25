"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""

import os, sys

HOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HOME not in sys.path:
    sys.path.append(HOME)

import OS_ENVIRON
os.environ.setdefault('COLLECTIVE_NAME', 'wsgi')
#os.environ.setdefault('LOG_CONFIG', os.path.join(HOME, os.environ['CONF'], 'log.wsgi.conf'))


"""
from django.conf import settings
import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()
def application(environ, start_response):
    if len(settings.PREFIX_URL) > 0:
        environ['PATH_INFO'] = environ['PATH_INFO'].replace(settings.PREFIX_URL, '', 1)
    return _application(environ, start_response)
"""


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
