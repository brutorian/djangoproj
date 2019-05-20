# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import ContactForms
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
    title = 'Contact Us'
    form = ContactForms(request.POST or None)
    context = {'title': title, 'form': form,}

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from Unicode.com' #in email should say from Unicode.com
        message = '%s %s' %(comment, name) #Show name of sender and the comment
        emailFrom = form.cleaned_data['email'] #Who email is from
        emailTo = [settings.EMAIL_HOST_USER] #connect to the EMAIL_HOST_USER
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)#post the message
        title = "Thank you"#returns message once submitted
        confirm_message = "We'll be in touch soon"#extra message
        context = {'title': title, 'confirm_message': confirm_message,}#once submitted title and extra message shown
    return render(request,'contact/contact.html',context)#return page