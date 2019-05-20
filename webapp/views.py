# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.conf import settings
#import stripe


def home(request):
        return render(request, 'index.html', context=None)

def about(request):
    return render(request, 'about.html', context=None)

def support (request):
    return render(request, 'support.html', context=None)
    
