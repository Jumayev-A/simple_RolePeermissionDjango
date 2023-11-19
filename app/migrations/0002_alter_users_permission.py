# Generated by Django 4.2.7 on 2023-11-19 14:24

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='permission',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Create'), (2, 'Red'), (3, 'Update'), (4, 'Delete')], editable=False, max_length=10),
        ),
    ]