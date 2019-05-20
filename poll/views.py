# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def poll(request):
    latest_questions = Question.objects.order_by('-pub_date')[:8]#order by date and number shown on page
    context = {'latest_questions': latest_questions}#show newest polls
    return render(request, 'poll/poll.html', context) #main poll page, like blog shows list of questions

@login_required(login_url='/accounts/login/')
def detail_poll(request, question_id):
    question = get_object_or_404(Question, pk = question_id)#used pk as slug kept giving errors
    return render(request, 'poll/detail_poll.html', {'question': question})#show options answers

@login_required(login_url='/accounts/login/')
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'poll/results.html', {'question': question})#show results

@login_required(login_url='/accounts/login/')
def vote(request, question_id):
    question  = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk= request.POST['choice'])
    except:
        return render(request, "poll/detail_poll", {'question':question, 'error_message': "Please select a choice"})
    else:
        selected_choice.votes += 1 #adds one vote for each submission
        selected_choice.save() #save the number of votes

        return HttpResponseRedirect(reverse('poll:results', args=(question.id,))) #the vote redirect to results page
