from django.conf.urls import *
from django.http import HttpResponse
from django.contrib import admin
from django.contrib.sites.models import Site
admin.autodiscover()
admin.site.unregister(Site)

import web

urlpatterns = [
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    url(r'^home/', include('home.urls'))
]
