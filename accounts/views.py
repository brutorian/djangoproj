# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        next = request.GET.get('next')
        if form.is_valid():
            form.save()
            #Register User
            username = form.cleaned_data.get('username')#require username
            raw_password = form.cleaned_data.get('password1')#require password
            user = authenticate(username=username, password=raw_password)
            #Once signed up automatically logged in
            login(request, user)#login uses user
            #return to home page
            return redirect('/')#signed up redirects to index

    if request.user.is_authenticated:#go to home page if logged in
         return redirect('/')
    else:#if fail return to signup
        form = UserCreationForm()
    return render(request,'accounts/signup.html', {'form' : form})#stay on signup page if fail


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login user
            user = form.get_user()#collect user
            login(request,user)#collect password from user
            return redirect('/')#redirect to index page
    if request.user.is_authenticated:#if already logged in return home page
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})#stay on login page if fail

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
