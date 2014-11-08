"""
Django settings for tagsys project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'tagsys/templates'),
)

ADMINS = (
    ('<your-name>', '<your-email-address>'), # generalized for security purposes
)
EMAIL_SUBJECT_PREFIX = '[Django Helpdesk]'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2krgecaa4zlc+#m+$iiiwlytm!e^l!j8+ci)&pgq*dwvq@yb#('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tagsys',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'helpdesk-web.urls'

WSGI_APPLICATION = 'helpdesk-web.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
	'USER': '<your-db-username>', # generalized for security purposes
	'PASSWORD': '<your-db-password>', # generalized for security purposes
	'HOST': '<your-db-host>', # generalized for security purposes
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Rest Framework Configuration
REST_FRAMEWORK = {
    'PAGINATE_BY': 100,
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
}

# LDAP Authenication Configurations

import ldap
import string
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, PosixGroupType

# AUTH_LDAP_START_TLS = True
AUTH_LDAP_GLOBAL_OPTIONS = {
    ldap.OPT_X_TLS_REQUIRE_CERT: False,
    ldap.OPT_REFERRALS: False,
}

AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_DEBUG_LEVEL: 0,
    ldap.OPT_REFERRALS: 0,
}

# Baseline Configuration
AUTH_LDAP_SERVER_URI = "ldaps://<your-ldap-host>:636" # generalized for purposes
AUTH_LDAP_BIND_DN = "<your-ldap-bind-dn>" # generalized for security purposes
AUTH_LDAP_BIND_PASSWORD = "<your-ldap-bind-dn-password>" # generalized for security purposes
AUTH_LDAP_USER_SEARCH = LDAPSearch("<your-base-dn>", ldap.SCOPE_SUBTREE, "(uid=%(user)s)") # generalized for security purposes
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Basic Group Parameters
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("<ldap-group-ou>", ldap.SCOPE_SUBTREE, "objectClass=groupOfNames") # generalized for security purposes
# Set Group Type
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()
# Simple Group Restrictions
AUTH_LDAP_REQUIRE_GROUP = "<ldap-group-ou>" # generalized for security purposes

# Populate the Django User from the LDAP directory
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "cn",
    "email": "mail",
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_staff": "<ldap-group-ou>", # generalized for security purposes
    "is_superuser": "<ldap-group-ou>", # generalized for security purposes
}

AUTH_LDAP_MIRROR_GROUPS = True
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache group memberships for an hour to minimize LDAP traffic
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600

# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_auth_ldap.backend.LDAPBackend',
)

# Logging Information
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'stream_to_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_auth_ldap': {
            'handlers': ['stream_to_console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

