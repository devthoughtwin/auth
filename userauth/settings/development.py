from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'login',
        'USER': 'postgres',
        'PASSWORD': 'psql',
        'HOST': 'db',
        'PORT': '5432',
    }
}


try:
    from .local import *
except Exception as e:
    pass