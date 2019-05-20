# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404, reverse
from.models import Blog
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CommentForm


# Create your views here.
def blog_list(request):
    blog = Blog.objects.all().order_by('date') #This will order blogs by date
    return render(request,'blog/blog_list.html', {'blog':blog})#Renders blogs on the template

@login_required(login_url='/accounts/login/')
def blog_detail(request, slug):
    #return HttpResponse(slug)#Return the slug urls for the detail pages
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog/blog_detail.html', {'blog':blog})

@login_required(login_url='/accounts/login/')
def blog_comment(request, slug):
    blog = get_object_or_404(Blog, slug=slug)#return 404 is for exceptions
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()#save comment
            return redirect('blog:detail', slug=blog.slug)#redirect to page after save
        else:
            form = CommentForm()
            context = {'form':form}#comment from
            return render(request, 'blog/comment.html', context)#page form on

    return render(request, 'blog/comment.html')

