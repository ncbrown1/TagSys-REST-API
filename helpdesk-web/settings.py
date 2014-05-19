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

ADMINS = (
    ('Nick Brown', 'ncbrown@engineering.ucsb.edu'),
)
EMAIL_SUBJECT_PREFIX = '[Django Helpdesk]'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2krgecaa4zlc+#m+$iiiwlytm!e^l!j8+ci)&pgq*dwvq@yb#('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['chef.cs.ucsb.edu', 'corral.engr.ucsb.edu', 'hanshan.cs.ucsb.edu']


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
	'USER': 'test_user',
	'PASSWORD': 'ncbrownpassword',
	'HOST': 'deepthought.cs.ucsb.edu',
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
AUTH_LDAP_SERVER_URI = "ldaps://ldap4.engr.ucsb.edu:636"
AUTH_LDAP_BIND_DN = "uid=nssldap,ou=people,dc=engr,dc=ucsb,dc=edu"
AUTH_LDAP_BIND_PASSWORD = "buMps3tSp1ke"
AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=engr,dc=ucsb,dc=edu", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Basic Group Parameters
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=engr,dc=ucsb,dc=edu", ldap.SCOPE_SUBTREE, "objectClass=groupOfNames")
# Set Group Type
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()
# Simple Group Restrictions
# AUTH_LDAP_REQUIRE_GROUP = "cn=coe-admin,ou=people,dc=engr,dc=ucsb,dc=edu"

# Populate the Django User from the LDAP directory
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "cn",
    "email":"mail",
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_staff":"cn=coe-admin,ou=groups,dc=engr,dc=ucsb,dc=edu",
    "is_superuser": "cn=coe-admin,ou=groups,dc=engr,dc=ucsb,dc=edu",
#    "is_superuser": "cn=coe-admin,ou=groups,dc=engr,dc=ucsb,dc=edu",
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
