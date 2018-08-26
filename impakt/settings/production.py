from .base import *
from .config import CONFIG
from .secrets import SECRETS

ALLOWED_HOSTS = ['*']
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': CONFIG['DATABASE_ENGINE'],
        'NAME': SECRETS['DATABASE_NAME'],
        'USER': SECRETS['DATABASE_USER'],
        'PASSWORD': SECRETS['DATABASE_PASSWORD'],
        'PORT': SECRETS['DATABASE_PORT'],
        'HOST': SECRETS['DATABASE_HOST'],
    }
}
