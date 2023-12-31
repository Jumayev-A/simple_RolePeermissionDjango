from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
import uuid

# Create your models here.


Permissions = (
        ('createRole', 'Topar goşmak'),
        ('viewRole', 'Topar görmek'),
        ('updateRole', 'Topar üýtgetmek'),
        ('deleteRole', 'Topar pozmak'),
        ('createUser', 'Ulanyjy goşmak'),
        ('viewUser', 'Ulanyjy görmek'),
        ('updateUser', 'Ulanyjy üýtgetmek'),
        ('deleteUser', 'Ulanyjy pozmak'),
    )

class Role(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=25, unique=True)
    permission = MultiSelectField(choices=Permissions, max_length=10, unique=True)
    users = models.ManyToManyField(User, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1, unique=True)
    roles = models.ManyToManyField(Role, blank=True)

    def __str__(self):
        return self.user.username

class AccountPermission(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    permission = MultiSelectField(choices=Permissions, max_length=10, null=True, blank=True)

    def __str__(self):
        return self.user.username
    




