from django.conf.urls import patterns, url
from gettogether_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^events/$', views.events, name='events'))