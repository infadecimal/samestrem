DEBUG = True

HOST = "http://samestrem.vagrant.internal"

# Database Settings
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'samestrem',
        'USER': 'samestrem',
        'PASSWORD': 'samestrem',
        'HOST': 'localhost'
    },
    }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
    }
}

CACHE_MIDDLEWARE_SECONDS = 60*60
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

# Session Settings
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

SESSION_COOKIE_DOMAIN = 'samestrem.vagrant.internal'

SESSION_COOKIE_SECURE = True

MEDIA_ROOT = '/srv/www/samestrem/media/'
MEDIA_URL = '/media/'

STATIC_ROOT = '/srv/www/samestrem/static_collected/'
STATIC_URL = '/static_collected/'
STATICFILES_DIRS = ['/srv/www/samestrem/web/static']

# Suffix appended to all page titles.
SITE_TITLE = 'Sam Estrem'

# IDs of groups that can see all locations, programs, and events,
# regardless of user or group ownership.
ALL_ACCESS_GROUP_IDS = [1, 2, 7, 39]

# ID of group that can log in by impersonating other users.
IMPERSONATE_GROUP_ID = 22

# IDs of groups that new public users should automatically join.
NEW_USER_GROUPS = [3]

