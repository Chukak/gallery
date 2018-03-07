"""
Production settings.

Note: import only base setting. Don`t use this for something else.
"""
from .base import *

DEBUG = False

ALLOWED_HOSTS = []

# Mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'mysql.cnf'),
        },
    }
}
