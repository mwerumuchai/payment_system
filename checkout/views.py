from __future__ import absolute_import
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction
from django.http import Http404
from django.urls import reverse

# Create your views here.
def index(request):
    '''
    Function that gets a list of Profile details
    '''

    return render(request,'index.html')

@login_required
def checkout(request,username):
    try:
        user = User.objects.get(username=username)

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'checkout.html')
