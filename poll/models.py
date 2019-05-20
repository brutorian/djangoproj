# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')#shows time question was made

    def __unicode__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=300)#answer choices usually multiple
    votes = models.IntegerField(default=0)#how many votes were given
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#delete the question

    def __unicode__(self):
        return self.choice_text
