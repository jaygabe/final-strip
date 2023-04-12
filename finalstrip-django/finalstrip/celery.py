import os
import sys

import django
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finalstrip.settings.local")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors_api.settings.production")

app = Celery("finalstrip")

app.config_from_object("django.conf:settings", namespace="CELERY")

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
# django.setup()

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)