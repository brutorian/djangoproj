# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import  include, url
from django.contrib import admin
from . import views
app_name = 'payment'

urlpatterns = [
url(r'^$', views.payment, name="payment"), #pay url
url(r'^success/$', views.success, name="success"), #success pay url
]
