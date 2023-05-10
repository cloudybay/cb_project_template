"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

from dotenv import load_dotenv
load_dotenv()

from django.core.wsgi import get_wsgi_application

from cb import log

collective_name = "wsgi"
log.set_collective_name(collective_name)
log.verbose("using collective name:", collective_name)

application = get_wsgi_application()
