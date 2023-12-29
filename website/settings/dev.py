from . base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f#-c2p)@y2f$ki%p=8f+=k^xoo@@6-j+ugu(6q^9dqz!7*vj()'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATIC_DIR = os.path.join(BASE_DIR, 'Public')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'Public/Media')
STATICFILES_DIRS = [STATIC_DIR]