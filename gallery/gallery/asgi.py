import os
import django
from channels.routing import get_default_application

# setting channels
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery.settings.development")
django.setup()
application = get_default_application()
