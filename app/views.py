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
        "group_page_active": "active",
        "groups": models.Role.objects.filter(is_active=True).order_by("-id"),
    }
    return render(request, 'group.html', context)

@login_required(login_url='/login/')
def group_add(request):
    context = {
        "title": "Topar goş",
        "group_page_active": "active"
    }
    permissions = models.Permissions
    users = User.objects.all().exclude(is_superuser=True)
    context['permissions'] = permissions
    context['users'] = users
    if request.method == "POST":
        group_name = request.POST.get('group_name')
        permissions = request.POST.getlist('permissions')
        users = request.POST.getlist('users')
        
        group = models.Role.objects.get_or_create(name=group_name, permission=permissions)
        
        if len(users) > 0:
            for user in users:
                u = models.Account.objects.get(user=User.objects.get(username=user))
                u.roles.add(group)
                u.save()
        print(group_name, permissions, users)
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