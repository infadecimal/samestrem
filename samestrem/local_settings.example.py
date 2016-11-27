DEBUG = True

# Contact Email
CRM_TO_EMAIL = 'jaldrich@samestrem.com'
SALES_TO_EMAIL = 'jaldrich@samestrem.com'

# Database Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'samestrem',
        'USER': 'root',
    }
}

API_HOST = 'localhost:8912'


# Turn on Cache
CACHE_BACKEND = 'memcached://www3:11311;www4:11311;www5:11311/'
CACHE_MIDDLEWARE_SECONDS = 60*60
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

# Session Settings
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_DOMAIN = '.samestrem.com'

# Email Configuration
EMAIL_SUBJECT_PREFIX = '[samestrem@www3] '

# Suffix appended to all page titles.
SITE_TITLE = 'Sam Estrem'

# Geocoder socket server connection settings.
GEOCODER_HOST = 'database0'
GEOCODER_PORT = 3411

# IDs of groups that can see all locations, programs, and events,
# regardless of user or group ownership.
ALL_ACCESS_GROUP_IDS = [1, 2, 7, 39]

# ID of group that can log in by impersonating other users.
IMPERSONATE_GROUP_ID = 22

# IDs of groups that new public users should automatically join.
NEW_USER_GROUPS = [3]

# The values of these settings will not get displayed on exception reports.
class PRIVATE:

    # API master key
    API_SALT = '...'

    # Upcoming API settings
    UPCOMING_GATEWAY_URL = 'http://database0:8511/'
    UPCOMING_USER_ID = 533814
    UPCOMING_TOKEN = '...'
    UPCOMING_DEFAULT_CATEGORY_ID = 10
    UPCOMING_DEFAULT_TAGS = 'recycle'
