"""
WSGI config for vk_save project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

# +++++++++++ DJANGO +++++++++++
import os
import sys

## assuming your Django settings file is at '/home/my_username/projects/my_project/settings.py'
path = '/home/oyvsyo/vk_save'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'my_project.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()