"""
Django settings for backend project.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -----------------------------------------------------------------------------
# Security Settings
# -----------------------------------------------------------------------------
SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = os.getenv("DEBUG", False)
ALLOWED_HOSTS = [os.environ["DOMAIN"],'localhost']
ENV_NAME = os.environ["ENV_NAME"]

# -----------------------------------------------------------------------------
# Application Definition
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'webpack_loader',
    'api',
    'django_filters',
    'maintenance_mode',
    'massadmin'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'project.customheaderauth.CustomHeaderMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'maintenance_mode.middleware.MaintenanceModeMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'project.wsgi.application'

# -----------------------------------------------------------------------------
# Database
# -----------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3') if os.getenv("CONFIG_DIR") is None else os.path.join(os.getenv("CONFIG_DIR", "db.sqlite3")),
    }
}

# -----------------------------------------------------------------------------
# Rest Framework Security
# -----------------------------------------------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
}

# -----------------------------------------------------------------------------
# Password Validation
# -----------------------------------------------------------------------------
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

AUTHENTICATION_BACKENDS = [
    'project.customheaderauth.CustomHeaderBackend',
]


# -----------------------------------------------------------------------------
# Internalization
# -----------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -----------------------------------------------------------------------------
# Static Files (i.e. CSS, images, JavaScript)
# -----------------------------------------------------------------------------

# Directories to look for when collecting static files
# Note: We include both the Webpack compiled static files from the frontend
#       as well as any shared static files between frontend and backend
STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), "frontend/dist"),
]

# URL endpoint for accessing static files
STATIC_URL = "/static/"

# Directory where collected static files will reside
# Note: the actual directory where the files reside may be different
# from the URL path used to access them!
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'public')

# Configure the Webpack loader plugin
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "/",
        "STATS_FILE": os.path.join(
            os.path.dirname(BASE_DIR), "frontend/webpack-stats.json"),
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
    }
}

# -------------------------------------------------------------------------------
# Media Files (PDFs)
# -------------------------------------------------------------------------------

# URL endpoint for accessing media files
MEDIA_URL = '/media/'

SITE_ID = 2

# Directory where media files will reside
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"backend/media")
