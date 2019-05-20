# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views
# Create your urls here.

app_name = 'contact'

urlpatterns = [
    url(r'^contact/$', views.contact, name="contact"),#contact url
]
