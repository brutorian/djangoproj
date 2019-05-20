# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render
import stripe
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required(login_url='/accounts/login/')
def payment(request):
    publishkey = settings.STRIPE_PUBLISHABLE_KEY #connects to STRIPE_PUBLISHABLE_KEY in settings
    context = {'publishkey': publishkey}
    if request.method == 'POST':
        token = request.POST['stripeToken'] #request token
        charge = stripe.Charge.create(
            amount=1999, #amount to be payed
            currency='gbp', #payment currency
            description='Donation',
            source=token,
            statement_descriptor='Donation to the site',
        )
        return render(request, 'payment/success.html') #complete pay return success page

    return render(request, 'payment/payment.html', context)

@login_required(login_url='/accounts/login/')
def success(request):
    return render(request, 'payment/success.html')