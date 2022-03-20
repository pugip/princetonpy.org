"""
WSGI config for princetonpy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from hypercorn.middleware import AsyncioWSGIMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "princetonpy.settings")

wsgi_app = get_wsgi_application()
application = AsyncioWSGIMiddleware(wsgi_app)
