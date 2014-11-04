# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth import *
from django.shortcuts import redirect
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def first_page(request):
    return HttpResponse("<h1>Bazinga!</h1>")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)   # maybe need to modify the field

def diff_response(request):
    if request.user.is_authenticated():
        content = "<p>my dear user</p>"
    else:
        content = "<p>you wired stranger</p>"
    return HttpResponse(content)	

@login_required
def user_only(request):
    return HttpResponse("<p>This message is for logged in user only.</p>")
	
def user_login(request):
    '''
    login view.
    '''
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = password = ''
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user     = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)    # come from django.contrib.auth
                return diff_response(request)
            else:
                return diff_response(request)
    form = LoginForm()
    ctx = {}
    ctx.update(csrf(request))
    ctx['form'] = form
    return render(request, 'login.html', ctx)

def user_logout(request):
    '''
    logout
    URL: /users/logout
    '''
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
        return redirect('/')
    else:
        form = UserCreationForm()
        ctx = {'form': form}
        ctx.update(csrf(request))
        return render(request, 'register.html', ctx)


