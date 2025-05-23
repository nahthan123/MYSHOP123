"""
WSGI config for MyShop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyShop.settings')

application = get_wsgi_application()
import django
django.setup()

from django.core.management import call_command

try:
    call_command('migrate')
    call_command('collectstatic', interactive=False)
except Exception as e:
    print(f"Migration/static error: {e}")
