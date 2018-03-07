from models import User
from django.contrib import messages
from bs4 import BeautifulSoup as bs
import json
import bcrypt
import request
from datetime import datetime
from django.shortcuts import render, redirect

def index(request):
    return render (request, 'index.html')

def login(request):
    email = request.POST["email"]
    password = request.POST["password"]
    check = User.objects.login(email, password)
    if check == True:
        user = User.objects.get(email = email)
        request.session["current_user"] = user.id
        return redirect('/nba_news')
    else:
        messages.warning(request, check[0])
        return redirect('/')

def logout(request):
    request.session['current_user'] = 0
    return redirect('/')

def registration(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    password = request.POST["password"]
    confirm_password = request.POST["confirm_password"]
    check = User.objects.register(first_name, last_name, email, password, confirm_password)
    if check == True:
        pwhashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pwhashed)
        request.session["current_user"] = user.id
        return redirect("/nba_news")
    else:
        for i in range(0, len(check)):
            messages.warning(request, check[i])
        return redirect("/")