# Generated by Django 4.2.7 on 2023-11-29 14:57

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_role_users_alter_role_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpermission',
            name='permission',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('create', 'CREATE'), ('red', 'RED'), ('update', 'UPDATE'), ('delete', 'DELETE')], max_length=10, null=True),
        ),
    ]