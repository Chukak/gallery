import os
import django
from channels.routing import get_default_application

# setting channels
# check https://channels.readthedocs.io/en/latest/
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery.settings")
django.setup()
application = get_default_application()
