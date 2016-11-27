import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

class PRIVATE:
    # API master key
    API_SALT = 'mr.sam'

    # Upcoming API settings
    UPCOMING_GATEWAY_URL = 'http://localhost:8511/'
    UPCOMING_USER_ID = 533814
    UPCOMING_TOKEN = 'bd235b11acfc8c10be8addc520dd6af5ec7972d4'
    UPCOMING_DEFAULT_CATEGORY_ID = 10
    UPCOMING_DEFAULT_TAGS = 'recycle'

# Django settings for samestrem project.
DEBUG = True
INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    ('Developer', 'andy@parthenonsoftware.com'),
)

ADMIN_DEFAULT_FILTERS = {}

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'Sam Estrem <noreply@samestrem.com>'

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Phoenix'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
###ADMIN_MEDIA_PREFIX = '/media/'

# Account Activation System Settings
ACCOUNT_ACTIVATION_DAYS = 5

# Email Configuration
EMAIL_HOST = 'localhost'
EMAIL_SUBJECT_PREFIX = '[samestrem] '

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8#ks_c5a35a=uadnkabk@g)e6&-h1&0@-0wpz(kg+h_76da3ow'

# Order matters! Please ensure that UpdateCacheMiddleware is first and
# FetchFromCacheMiddleware is last.
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'web.middleware.threadlocals.ThreadLocals',
    'web.middleware.minify_html.MinifyHTMLMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'web.middleware.filter_persist.FilterPersistMiddleware',
    'web.middleware.profile.ProfileMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
  )

COMPRESS_HTML = True

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {   
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }
]

COMPRESS_PRECOMPILERS = (
   ('text/less', 'lessc {infile} {outfile}'),
)

ALLOWED_HOSTS = [
    "192.168.111.222",
    "samestrem.vagrant.internal"
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions', 'django.contrib.sites', 'django.contrib.staticfiles',
    'form_utils',
    'compressor',
    'static_precompiler'
)

SERIALIZATION_MODULES = {
    'json': 'web.wadofstuff.django.serializers.json'
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True

AUTH_PROFILE_MODULE = 'registration.registrationprofile'
LOGIN_REDIRECT_URL = '/'

TOS_AGREEMENT_URL = '/accounts/tos/'
TOS_AGREEMENT_VERSION = 5

# Suffix appended to all page titles.
SITE_TITLE = 'Sam Estrem'

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
#try:
from local_settings import *
#except ImportError:
#    pass

# Enable debug toolbar for debug mode.
if DEBUG:
    # def custom_show_toolbar(request):
    #     return True # Always show toolbar, for example purposes only.
    # MIDDLEWARE_CLASSES = \
    #     (MIDDLEWARE_CLASSES[:-3] +
    #     ('debug_toolbar.middleware.DebugToolbarMiddleware',) +
    #     MIDDLEWARE_CLASSES[-3:])
    # INSTALLED_APPS += ('debug_toolbar',)
    # DEBUG_TOOLBAR_CONFIG = {
    #     'INTERCEPT_REDIRECTS': False,
    #     'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    # }
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
                'level': 'INFO',
            }
        }
    }
