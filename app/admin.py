from django.contrib import admin
# from app.models import Roles, Account, TestModel
# # Register your models here.


# @admin.register(Account)
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ['user',]

# @admin.register(Roles)
# class RolesAdmin(admin.ModelAdmin):
#     list_display = ['role_name', 'permissions',]

# @admin.register(TestModel)
# class TestModelAdmin(admin.ModelAdmin):
#     list_display = ['name', 'desc',]

from app import models

@admin.register(models.Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['permissions',]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        for role in models.Role.objects.filter(permission__id=obj.id):
            role_permission = role.permission
            for user in models.Users.objects.filter(roles=role):
                
                print(type(user.permission), 100*"=")

@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', "list_permissions"]

    def list_permissions(self, obj):
        return ",".join([p for p in obj.permission.permissions])

@admin.register(models.Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['user','list_permissions',]
    readonly_fields = ['permission',]

    def list_permissions(self, obj):
        return ",".join([p for p in obj.permission])

    def save_model(self, request, obj, form, change):
        user_permission = []
        user_roles = request.POST.getlist("roles")
        for role_id in user_roles:
            for i in models.Role.objects.get(id=role_id).permission.permissions:
                if i not in user_permission:
                    user_permission.append(i)
        obj.permission = user_permission
        super().save_model(request, obj, form, change)