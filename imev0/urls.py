__author__ = 'MiladDK'

from django.conf.urls import url
from .views import *



urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^datas$', Datas.as_view(), name='getDatas'),
    url(r'^test$', Test.as_view(), name='test'),
    url(r'^maingourp$', MainGroupSums.as_view(), name='getGroups'),
    url(r'^mainOptions$', MainOptions.as_view(), name='getMainOptions'),
    url(r'^subOptions$', SubOptions.as_view(), name='getSubOptions'),
    url(r'^groupOptions$', GroupOptions.as_view(), name='getGroupOptions'),


]
