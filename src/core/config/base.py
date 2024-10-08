from pathlib import Path

from .helper.env_reader import env

BASE_DIR = Path(__file__).resolve().parent.parent

CORS_ORIGIN_ALLOW_ALL = True

# Production
PRODUCTION = env("PRODUCTION", default=False, cast=bool)

ALLOWED_HOSTS = ['*']


SECRET_KEY = env("SECRET_KEY")

THEME_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'debug_toolbar',
    'drf_yasg',
    'corsheaders',
    'djoser',
    'django_prometheus',
    'phonenumber_field',
]

THEME = [
    'jazzmin',
]

APPS = [
    'account',
    'profiles',
    'meditation',
    'ads',
    'administration',

]

INSTALLED_APPS = [
    *THEME,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *THEME_PARTY_APPS,
    *APPS
]
# MIDDLEWARE
MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

ROOT_URLCONF = 'core.urls'

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


AUTH_USER_MODEL = 'account.EsUser'

WSGI_APPLICATION = "core.wsgi.application"

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

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR.joinpath("static/")

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.joinpath("media/")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#JWT_SETTINGS 
from .helper.auth.jwt import *

#REST_FRAMEWORK_SETTINGS
from .helper.auth.rest_framework import *

#DJOSER_SETTINGS
from .helper.auth.djoser import *

#SMTP_SETTINGS
from .helper.auth.smtp import *

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'SUPPORTED_SUBMIT_METHODS': ['get', 'post', 'put', 'patch', 'delete', 'head', 'options'],
    'SWAGGER_UI_SETTINGS': {
        'supportedSubmitMethods': ['get', 'post', 'put', 'patch', 'delete', 'head', 'options'],
        'fileUpload': True,
    }
}


PHONENUMBER_DB_FORMAT = 'E164'
PHONENUMBER_DEFAULT_REGION = 'RU'

# CELERY_BROKER_URL = "redis://localhost:6379/0"
# CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

from .helper.cors import *

if not PRODUCTION:
    from .local import *
else:
    from .prod import *

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]


from .helper.jazzmin import JAZZMIN_SETTINGS