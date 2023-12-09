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
            messages.error(request, "Giriş şowsuz!")
    return render(request, 'login.html', context)


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('app:group')


# Group function
@login_required(login_url='/login/')
def group(request):
    context = {
        "title": "Toparlar",
        "group_page_active": "active",
        "groups": models.Role.objects.filter(is_active=True).order_by("-created"),
    }
    return render(request, 'group.html', context)

@login_required(login_url='/login/')
def group_add(request):
    context = {
        "title": "Topar goş",
        "group_page_active": "active",
        "permissions": models.Permissions,
        "users": User.objects.filter(is_active=True).exclude(is_superuser=True)
    }
    if request.method == "POST":
        group_name = request.POST.get('group_name')
        permissions = request.POST.getlist('permissions')
        users = request.POST.getlist('users')

        if (not models.Role.objects.filter(name=group_name).exists()) and (not models.Role.objects.filter(permission=permissions).exists()):
            group = models.Role.objects.create(name=group_name, permission=permissions)
            
            # Add Users in NewGroup
            for user in users:
                u = User.objects.get(username=user)
                group.users.add(u)
            group.save()

            # Sync new group in users
            for username in users:
                user_obj = User.objects.get(username=username)
                account = models.Account.objects.get(user=user_obj)
                account.roles.add(group)
                account.save()
                account_permission = models.AccountPermission.objects.get(user=user_obj)
                account_perm_list = list(account_permission.permission)
                for group_permission in permissions:
                    if group_permission not in account_perm_list:
                        account_perm_list.append(group_permission)
                account_permission.permission = account_perm_list
                account_permission.save()
            messages.success(request, "Topar gosuldy !")
        else:
            messages.info(request, "Bu gornusde topar eyyam bar !")
    return render(request, "group_add.html", context)

@login_required(login_url='/login/')
def group_update(request, id):
    context = {
        "title": "Topar goş",
        "group_page_active": "active",
        "permissions": models.Permissions,
        "users": User.objects.filter(is_active=True).exclude(is_superuser=True)
    }
    if models.Role.objects.filter(id=id).exists():
        group = models.Role.objects.get(id=id)
        context['group'] = group
        if request.method == "POST":
            group_name = request.POST.get('group_name')
            permissions = request.POST.getlist('permissions')
            users = request.POST.getlist('users')

            # Change group name
            if group.name != group_name:
                if not models.Role.objects.filter(name=group_name).exists():
                    group.name = group_name
            
            # Add group in user
            for new_user in users:
                new_user_obj = User.objects.get(username=new_user)
                new_account = models.Account.objects.get(user=new_user_obj)
                if not group.users.filter(username=new_user).exists():
                    print("ADD user")
                    new_account.roles.add(group)
                    new_account.save()

                new_account_permission = models.AccountPermission.objects.get(user=new_user_obj)
                new_account_perm_list = list(new_account_permission.permission)
                for permission in permissions:
                    if permission not in new_account_perm_list:
                        new_account_perm_list.append(permission)
                new_account_permission.permission = new_account_perm_list
                new_account_permission.save() 
            
            # Remove group in user
            for old_user in group.users.all():
                old_user_obj = User.objects.get(username=old_user)
                old_account = models.Account.objects.get(user=old_user_obj)
                if old_user.username not in users:
                    print("Remove user", users, old_user)
                    old_account.roles.remove(group)
                    old_account.save()

                old_account_permission = models.AccountPermission.objects.get(user=old_user_obj)
                old_account_perm_list = list(old_account_permission.permission)
                for group_permission in group.permission:
                    if group_permission in old_account_perm_list:
                        old_account_perm_list.remove(group_permission)
                old_account_permission.permission = old_account_perm_list
                old_account_permission.save()
                
            # change group permissions
            if group.permission != permissions:
                if not models.Role.objects.filter(permission=permissions).exists():
                    group.permission = permissions
                
            # Add new Users in Group
            group.users.clear()
            for user in users:
                u = User.objects.get(username=user)
                group.users.add(u)
            group.save()
            messages.success(request, "Topar uytgedildi !")
            return redirect("app:group")
    else:
        messages.error(request, "Topar tapylmady !")
        return redirect("app:group")
    return render(request, "group_update.html", context)

@login_required(login_url='/login/')
def group_delete(request, id):
    context = {
        "title": "Topar goş",
        "group_page_active": "active",
    }
    return render(request, "group_delete.html", context)

# User function
@login_required(login_url='/login/')
def users(request):
    context = {
        "title": "Ulanjylar",
        "users_page_active": "active",
        "users": models.Account.objects.filter(user__is_active=True).order_by("-id")
    }
    return render(request, 'users.html', context)

@login_required(login_url='/login/')
def users_add(request):
    context = {
        "title": "Ulanjy goşmak",
        "users_page_active": "active",
        "user_groups": models.Role.objects.filter(is_active=True),
        "user_permissions": models.Permissions,
    }
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        user_groups = request.POST.getlist("user_groups")
        user_permissions = request.POST.getlist("user_permissions")
        if not User.objects.filter(first_name=first_name, last_name=last_name, username=user_name).exists():
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, password=password)
        else:
            user = User.objects.get(first_name=first_name, last_name=last_name, username=user_name)
        if not models.Account.objects.filter(user=user).exists() and not models.AccountPermission.objects.filter(user=user).exists():
            account = models.Account.objects.create(user=user)
            
            # Add NewUser in Group
            for group_id in user_groups:
                group_obj = models.Role.objects.get(id=group_id)
                group_obj.users.add(user)
                group_obj.save()

            # Add Group in NewUser
            for user_group in user_groups:
                group = models.Role.objects.get(id=user_group)
                account.roles.add(group)
            account.save()

            # Add Permissions in NewUser
            account_permision = models.AccountPermission.objects.create(user=user)
            for user_group in user_groups:
                group = models.Role.objects.get(id=user_group)
                for group_permission in group.permission:
                    if group_permission not in user_permissions:
                        user_permissions.append(group_permission)
            account_permision.permission = user_permissions
            account_permision.save()
            messages.success(request, "Ulanyjy gosuldy !")
        else:
            messages.info(request, "Ulanyjy eyyam bar !")
    return render(request, 'users_add.html', context)