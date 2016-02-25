__author__ = 'MiladDK'

from django.conf.urls import url
from .views import Index, Datas, Test

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^datas$', Datas.as_view(), name='getDatas'),
    url(r'^test$', Test.as_view(), name='test'),


]
