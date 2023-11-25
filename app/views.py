from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from app import models
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:home')
        else:
            messages.error(request, "Login Failed!")
    return render(request, 'login.html', context)

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/login/')
def home(request):
    context = {
        "datas": None
    }
    return render(request, 'home.html', context)