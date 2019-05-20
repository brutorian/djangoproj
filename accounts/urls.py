# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url 
from . import views

app_name = 'accounts'

urlpatterns = [
 url(r'^signup/$',views.signup_view, name="signup"),#signup
 url(r'^login/$',views.login_view, name="login"),#login
 url(r'^logout/$',views.logout_view, name="logout"),

]
