# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if not 'current_user_id' in request.session:
        return redirect('/login')
    else:
        return redirect('/wall')

def login(request):
    return render(request, 'messages/login.html')

def add_user(request):
    pass


def add_friend(request):
    pass

def add_message(request):
    pass

def add(request):
    pass
