"""
WSGI config for gallery project.
Setting - gallery.settings.development module

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery.settings.development")

application = get_wsgi_application()
