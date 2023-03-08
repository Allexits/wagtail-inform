from .base import *


SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-+_@f-8v5nsz3gnwuh!m00&#x7m_yw913x@ob9wq)rpp!6!0s!0')

DEBUG = 'RENDER' not in os.environ

# Following settings only make sense on production and may break development environments.
if not DEBUG:    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

from inform.settings import urls

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urls.urlpatterns += staticfiles_urlpatterns()

