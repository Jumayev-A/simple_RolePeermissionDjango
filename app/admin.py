from django.contrib import admin
from app.models import Roles, Account, TestModel
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user',]

@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ['role_name', 'permissions',]

@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc',]