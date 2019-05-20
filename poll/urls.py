# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

app_name = 'poll'

# Create your views here.

urlpatterns = [
    url(r'^$', views.poll, name="poll"),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail_poll, name="detail_poll"),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]
