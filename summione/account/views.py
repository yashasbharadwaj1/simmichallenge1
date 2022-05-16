from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth


@login_required
def profile(request):
    return render(request,
                  'account/profile.html',
                  {'section': 'profile'})

