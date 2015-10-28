__author__ = 'perecullera'


from django.conf.urls import patterns, include, url
from hutsAPI import views

urlpatterns = patterns('',
                       url(r'^$',
                           views.index,
                           name='main'),)
