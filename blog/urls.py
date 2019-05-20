# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.blog_list, name="list"),#The blog list
    url(r'^(?P<slug>[\w-]+)/$',views.blog_detail, name="detail"),#The blog detailed page
    url(r'^(?P<slug>[\w-]+)/comment/$',views.blog_comment, name="comment"),#The blog comment page
]