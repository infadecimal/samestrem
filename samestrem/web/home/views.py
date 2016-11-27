from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template

from django.db import connections, transaction
from django.core.cache import cache # This is the memcache cache.


def index(request):
    return render(request, 'home/index.html', {"var":"World"})


def test(request):
    return render(request, 'home/test.html', {"var":"World"})
