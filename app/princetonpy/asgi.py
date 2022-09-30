"""
ASGI config for princetonpy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from hypercorn.middleware import AsyncioWSGIMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "princetonpy.settings")

# application = get_asgi_application()
wsgi_app = get_wsgi_application()
application = AsyncioWSGIMiddleware(wsgi_app)
