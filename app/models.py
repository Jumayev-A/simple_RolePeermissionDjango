from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.


class Roles(models.Model):
    Permissions = (
        (1, "Can Create"),
        (2, "Can Read"),
        (3, "Can Update"),
        (4, "Can Delete")
    )
    role_name = models.CharField(max_length=10, unique=True)
    permissions = MultiSelectField(choices=Permissions, max_length=10, unique=True)

    def __str__(self):
        return f"{self.role_name}"
    
    class Meta:
        verbose_name = 'Rollar'
        verbose_name_plural = "Rollar"




class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Roles, blank=True)

    class Meta:
        verbose_name = 'Ulanyjylar'
        verbose_name_plural = 'Ulanyjylar'

class TestModel(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=5)
    desc = models.TextField()

    def __str__(self):
        return self.name
