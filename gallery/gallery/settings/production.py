"""
Production settings.

Note: import only base setting. Don`t use this for something else.
"""
from .base import *

DEBUG = False

"""
Add your valid hosts here.

"""
ALLOWED_HOSTS = []

"""
Production has only mysql database.

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'mysql.cnf'),
        },
    }
}
