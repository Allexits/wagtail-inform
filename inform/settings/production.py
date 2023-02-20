from .base import *


SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-+_@f-8v5nsz3gnwuh!m00&#x7m_yw913x@ob9wq)rpp!6!0s!0')

DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


from inform.settings import urls

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()


