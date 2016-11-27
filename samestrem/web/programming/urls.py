from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^portfolio$', views.index, name='index'),
    url(r'^technologies$', views.index, name='index'),
]