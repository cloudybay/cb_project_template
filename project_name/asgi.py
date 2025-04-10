"""
ASGI config for bbb project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/asgi/
"""

from dotenv import load_dotenv
load_dotenv()

from django.core.asgi import get_asgi_application
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler

django_asgi_app = get_asgi_application()
application = ASGIStaticFilesHandler(django_asgi_app)
