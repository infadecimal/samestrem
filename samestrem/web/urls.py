from django.conf.urls import *
from django.http import HttpResponse
from django.contrib import admin
from django.contrib.sites.models import Site
admin.autodiscover()
admin.site.unregister(Site)

import web

urlpatterns = [
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    url(r'^$', include('home.urls')),
    url(r'^code/', include('programming.urls')),
    url(r'^dance/', include('dance.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^me/', include('me.urls'))
]
