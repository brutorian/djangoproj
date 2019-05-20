# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 120)#post title
    slug = models.SlugField()#url
    body = models.TextField()#main text
    date = models.DateTimeField(auto_now_add = True) #To automatically add time post was made
    #votes = models.VotableManager() #vote system used in polls

    def __unicode__(self):
        return self.title

    def snip(self):
        return self.body[:40] + '...'#Cuts down the amount of text shown on the blog

class Comments(models.Model):
    blog = models.ForeignKey(Blog, related_name='comment', on_delete=models.CASCADE)
    user = models.CharField(max_length=300)#comment user
    body = models.TextField()#main text
    created = models.DateTimeField(auto_now_add = True)#Add time comment made
    approved = models.BooleanField(default = False)#approves comment

    def approved(self):
        self.approved = True
        self.save()

    def __unicode__(self):
        return self.user



