"""
WSGI config for dental_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
# import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application

# if os.name == 'nt':
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dental_website.settings')
# else:
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dental_website.dental_website.settings')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dental_website.settings')


application = get_wsgi_application()
# application = django.core.handlers.wsgi.WSGIHandler()