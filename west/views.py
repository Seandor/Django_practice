# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf

from west.models import Character

from django import forms

def first_page(request):
    return HttpResponse("<p>西餐</p>")

def staff(request):
    staff_list = Character.objects.all()
    return render(request, 'templay.html', {'staffs': staff_list})

def templay(request):
    context 			= {}
    context['label']	= 'Hello World!'
    return render(request, 'templay.html', context)

def form(request):
    return render(request, 'form.html')

class CharacterForm(forms.Form):
    id   = forms.IntegerField()
    name = forms.CharField(max_length=200)
    sex  = forms.CharField(max_length=2)

def investigate(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            id_submitted = request.POST['id']
            name_submitted = request.POST['name']
            sex_submitted = request.POST['sex']
            new_record = Character(id=id_submitted, name=name_submitted, sex=sex_submitted)
            new_record.save()
    form = CharacterForm()
    ctx = {}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    ctx['form']  = form
    return render(request, 'investigate.html', ctx)
