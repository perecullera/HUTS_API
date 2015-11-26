__author__ = 'perecullera'


from django.conf.urls import patterns, include, url
from hutsAPI import views

urlpatterns = patterns('',
                       url(r'^$',
                           views.index,
                           name='main'),
                       url(r'^(?P<hut_id>[0-9]+)/$', views.detail, name='detail'),
                       url(r'^map/$',
                           views.map,
                           name='main'),
                       )
