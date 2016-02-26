__author__ = 'MiladDK'

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^datas$', Datas.as_view(), name='getDatas'),
    url(r'^test$', Test.as_view(), name='test'),
    url(r'^maingroup$', MainGroupSums.as_view(), name='getGroups'),


]
