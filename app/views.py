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
            messages.success(request, f"Salam, {username}")
            login(request, user)
            return redirect('app:group')
        else:
            messages.error(request, "Login Failed!")
    return render(request, 'login.html', context)

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('app:group')


# Group function
@login_required(login_url='/login/')
def group(request):
    context = {
        "datas": None,
        "title": "Toparlar",
        "group_page_active": "active"
    }
    return render(request, 'group.html', context)

@login_required(login_url='/login/')
def group_add(request):
    context = {
        "title": "Topar goş",
        "group_page_active": "active"
    }
    return render(request, "group_add.html", context)

# User function
@login_required(login_url='/login/')
def users(request):
    context = {
        "title": "Ulanjylar",
        "users_page_active": "active"
    }
    return render(request, 'users.html', context)

@login_required(login_url='/login/')
def users_add(request):
    context = {
        "title": "Ulanjy goşmak",
        "users_page_active": "active"
    }
    return render(request, 'users_add.html', context)