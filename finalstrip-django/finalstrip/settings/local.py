from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-bnw$7^@btnzaz+%=35va-=bv3gosvkroq2tpy@ct!xe_q_3qfw",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1" ]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000'
]

CSRF_TRUSTED_ORIGINS = ["http://*.localhost", "http://*.0.0.0.0", "http://*.127.0.0.1", 'http://localhost:3000' ]

ADMIN_URL = "admin/"

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "info@finalstrip.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Finalstrip"