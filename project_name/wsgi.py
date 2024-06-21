"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

from dotenv import load_dotenv
load_dotenv()

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
