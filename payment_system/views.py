from __future__ import absolute_import
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile,ContactRecipient
from .forms import contactForm,UserForm,ProfileForm
from .email import send_welcome_email
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

# @login_required
@transaction.atomic
def update_profile(request,username):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

# @login_required
def profile(request,username):
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'index.html')

# ABOUT
def about(request):
    '''
    Function that gets a about details
    '''

    # profiles = Profile.get_profile()
    return render(request,'about.html')

# Contact
# @login_required(login_url='/accounts/login/')
def contact(request):
    '''
    Function that gets a list of Profile details
    '''
    # profiles = Profile.get_profile()
    title = 'Contact'
    confirm_message = 'Thanks for the message. We will get right back to you'


    try:
        if request.method == 'POST':
            form = contactForm(request.POST)


            if form.is_valid():
                full_name = form.cleaned_data['full_name']
                email = form.cleaned_data['email']
                comment = form.cleaned_data['comment']


                recipient = ContactRecipient(full_name = full_name, email=email,comment=comment)
                recipient.save()
                send_welcome_email(full_name,email,comment)



                return render(request, 'contact.html',{'title':title,'confirm_message':confirm_message})

        else:
            form = contactForm()
        return render(request, 'contact.html',{'form':form,'title':title, })

    except Exception as exception:

        raise exception

    # LOGOUT
    def logout(request):
        return render(request, 'index.html')
