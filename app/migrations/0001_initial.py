# Generated by Django 4.2.7 on 2023-12-03 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25, unique=True)),
                ('permission', multiselectfield.db.fields.MultiSelectField(choices=[('createRole', 'Topar goşmak'), ('viewRole', 'Topar görmek'), ('updateRole', 'Topar üýtgetmek'), ('deleteRole', 'Topar pozmak'), ('createUser', 'Ulanyjy goşmak'), ('viewUser', 'Ulanyjy görmek'), ('updateUser', 'Ulanyjy üýtgetmek'), ('deleteUser', 'Ulanyjy pozmak')], max_length=10, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('createRole', 'Topar goşmak'), ('viewRole', 'Topar görmek'), ('updateRole', 'Topar üýtgetmek'), ('deleteRole', 'Topar pozmak'), ('createUser', 'Ulanyjy goşmak'), ('viewUser', 'Ulanyjy görmek'), ('updateUser', 'Ulanyjy üýtgetmek'), ('deleteUser', 'Ulanyjy pozmak')], max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.ManyToManyField(blank=True, to='app.role')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
