import os
from pathlib import Path
from datetime import timedelta
import environ

env = environ.Env()

ROOT_DIR = (
    Path(__file__).resolve().parent.parent.parent
)  # need three to get to manage.py level

# points django to where the apps are stored
APPS_DIR = ROOT_DIR / "journal_apps"

BASE_DIR = Path(__file__).resolve().parent.parent

# connects django to environment variables
environ.Env.read_env(os.path.join(ROOT_DIR / ".envs/.local/", ".django"))

DEBUG = env.bool("DJANGO_DEBUG", False)


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    "djcelery_email",
]

JOURNAL_APPS = [

    'journal_apps.authentication',
    'journal_apps.profiles',
    'journal_apps.journal',
    'journal_apps.social',
    'journal_apps.tournaments',
    'journal_apps.events',
    'journal_apps.bouts',
    'journal_apps.fencers',
    'journal_apps.usaf_data',
    'journal_apps.lessons',
    'journal_apps.common',

]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + JOURNAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # added
    'django.middleware.security.SecurityMiddleware',
    # "whitenoise.middleware.WhiteNoiseMiddleware", # added for production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "django.middleware.common.BrokenLinkEmailsMiddleware",  # added:  sends broken link notifications to managers
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'finalstrip.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'finalstrip.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {"default": env.db("DATABASE_URL")}
# DATABASES['default']['ATOMIC_REQUESTS'] = True

PASSWORD_HASHERS = [
    # "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    'django.contrib.auth.hashers.ScryptPasswordHasher',  # removed for some reason
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# change date format
DATE_FORMAT = '%m/%d/%Y'
USE_L10N = False

DATE_INPUT_FORMATS = (
    '%m/%d/%Y',     # '03/21/2014'
)
TIME_INPUT_FORMATS = (
    '%H:%M:%S',     # '17:59:59'
    '%H:%M',        # '17:59'
)
DATETIME_INPUT_FORMATS = (
    '%m/%d/%Y %H:%M',     # '03/21/2014 17:59'
)

# static and media
STATIC_URL = "/static/"
STATIC_ROOT = str(ROOT_DIR / "static")
STATICFILES_DIRS = []
STATICFILES_FINDERS = [  # these are defaults
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
MEDIA_URL = "/media/"
MEDIA_ROOT = str(ROOT_DIR / "media")

# cross site headers
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True  # allows us to use the cookie
SESSION_COOKIE_SAMESITE = None
CSRF_COOKIE_SAMESITE = None
CORS_URLS_REGEX = r"^/api/.*$" # only allows cors header on /api/

REST_FRAMEWORK = {
    'DATE_FORMAT': '%m/%d/%Y',
    'EXCEPTION_HANDLER':'journal_apps.authentication.exceptions.status_code_handler',  # makes all 403 http errors 401
}

# custom user model
AUTH_USER_MODEL = 'authentication.User'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'


#  Settings for setting up email later on
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_VERIFICATION = "none"
# myaccount.google.com/lesssecureapps   # this is now obsolete
# myaccount.google.com/apppasswords
# myaccount.google.com/DisplayUnlockCaptcha
EMAIL_HOST = '0.0.0.0'  # 'smtp.gmail.com
EMAIL_PORT = 1025 # 587 # port for gmail
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD =''
# EMAIL_USE_TLS = False # true for gmail
# EMAIL_USE_SSL = False


# Configuration for django logging of errors
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}
