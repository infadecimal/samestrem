from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^privatelessons$', views.index, name='index'),
    url(r'^experience$', views.index, name='index'),
    url(r'^qualifications$', views.index, name='index'),
]