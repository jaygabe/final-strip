from .base import *
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["finalstrip.com"])
ADMIN_URL = env("DJANGO_ADMIN_URL")

DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = []  # this needs to be filled out

SECURE_HSTS_SECONDS = 60

SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)

# do not try to predict content type
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

# exclusively use SSL
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Finalstrip Support <support@finalstrip.com>",
)

SITE_NAME = "Finalstrip"

# default email for error messages
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="Final Strip",
)

# similar to local.py these are the settings for the mailgun configuration
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = "smtp.mailgun.org"
EMAIL_HOST_USER = "postmaster@mg.finalstrip"
EMAIL_HOST_PASSWORD = env("SMTP_MAILGUN_PASSWORD")
EMAIL_PORT = 587 # mailgun tells you in Sending > Domain settings > SMTP credentials.  also port 25.
EMAIL_USE_TLS = True # encrypts emails for privacy
DOMAIN = env("DOMAIN")


# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}


# myaccount.google.com/lesssecureapps   # this is now obsolete
# myaccount.google.com/apppasswords
# myaccount.google.com/DisplayUnlockCaptcha

# EMAIL_HOST = '0.0.0.0'  # 'smtp.gmail.com
# EMAIL_PORT = 1025 # 587 # port for gmail
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD =''
# EMAIL_USE_TLS = False # true for gmail
# EMAIL_USE_SSL = False