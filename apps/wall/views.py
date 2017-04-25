# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message

# Create your views here.

def index(request):
    if not 'current_user_id' in request.session:
        return redirect('/loginpage')
    else:
        return redirect('/wall')

def wall(request):
    context = {
    'user': User.objects.get(id=request.session['current_user_id'])
    }
    return render(request, 'messages/wall.html', context)

def login_page(request):
    return render(request, 'messages/login.html')

def login(request):
    email=request.POST["email"]
    password=request.POST["password"]
    login1={
        "email": email,
        "password": password
    }
    check=User.objects.validate_login(login1)
    if check:
        for i in range (0, len(check)):
            messages.add_message(request, messages.INFO, check[i])
        return redirect ('/login')
    user1=User.objects.filter(email=email, password=password)
    request.session["current_user_id"]=user1[0].id
    print "hi"
    return redirect('/wall')

def register(request):
    first_name=request.POST["first_name"]
    last_name=request.POST["last_name"]
    email=request.POST["email"]
    password=request.POST["password"]
    confirm_pw=request.POST["confirm_pw"]
    user1 = User.objects.filter(email = email)
    if user1:
        messages.add_message(request, messages.INFO, "Email exists, please login")
        return redirect ('/login')
    register1 = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "confirm_pw": confirm_pw
    }
    check = User.objects.validate_registration(register1)
    if check:
        for x in range(0, len(check)):
            messages.add_message(request, messages.INFO, check[x])
        return redirect ('/login')
    user2=User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
    request.session["current_user_id"]=user2.id
    print "hi"
    return redirect ('/wall')

def logout(request):
    request.session.clear()
    return redirect ('/login')

def add_friend(request):
    pass

def add_message(request):
    if (request.POST['comment']):
        Message.objects.create(content=request.POST['comment'], user=User.objects.get(id=request.session['current_user_id']))
    return redirect('/wall')
