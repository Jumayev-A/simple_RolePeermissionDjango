from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.


Permissions = (
        (1, 'Create'),
        (2, 'Red'),
        (3, 'Update'),
        (4, 'Delete'),
    )


class Permission(models.Model):
    permissions = MultiSelectField(choices=Permissions, max_length=10)

    class Meta:
        verbose_name = 'Rugsat'
        verbose_name_plural = 'Rugsat'

class Role(models.Model):
    name = models.CharField(max_length=25)
    permission = models.OneToOneField(Permission, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Rol'

class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    roles = models.ManyToManyField(Role, blank=True)
    permission = MultiSelectField(choices=Permissions, max_length=10)

# class UserPermission(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     permission = MultiSelectField(choices=Permissions, max_length=10)



