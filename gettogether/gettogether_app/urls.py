from django.conf.urls import patterns, url
from gettogether_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^events/$', views.events, name='events'),
        url(r'^games/$', views.games, name='games'),
        url(r'^useful_links/$', views.useful_links, name='useful_links'),
        url(r'^forum/$', views.forum, name='forum'))