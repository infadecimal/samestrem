from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bio$', views.index, name='bio'),
    url(r'^education$', views.index, name='education'),
]