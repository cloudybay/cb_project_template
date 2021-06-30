"""
WSGI config for cbgears project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

from dotenv import load_dotenv
load_dotenv()

from cb import log
from cb.util import config
log.set_log_config(config.get_abs_path('log.conf'))

collective_name = "wsgi"
log.set_collective_name(collective_name)
log.verbose("using collective name:", collective_name)

from django.conf import settings
from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application()
def application(environ, start_response):
    if settings.FORCE_SCRIPT_NAME:
        environ['PATH_INFO'] = environ['PATH_INFO'].replace(
            settings.FORCE_SCRIPT_NAME, '', 1)
    return _application(environ, start_response)
