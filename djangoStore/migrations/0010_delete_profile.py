# Generated by Django 5.0 on 2024-01-18 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoStore', '0009_remove_profile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
