from django.contrib import admin
from app import models

admin.site.register(models.Account)
admin.site.register(models.AccountPermission)

@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', "permission",]

# @admin.register(models.Users)
# class UsersAdmin(admin.ModelAdmin):
#     list_display = ['user','list_permissions',]
#     readonly_fields = ['permission',]

#     def list_permissions(self, obj):
#         return ",".join([p for p in obj.permission])

#     def save_model(self, request, obj, form, change):
#         user_permission = []
#         user_roles = request.POST.getlist("roles")
#         for role_id in user_roles:
#             for i in models.Role.objects.get(id=role_id).permission.permissions:
#                 if i not in user_permission:
#                     user_permission.append(i)
#         obj.permission = user_permission
#         super().save_model(request, obj, form, change)