# Generated by Django 5.0 on 2024-01-18 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoStore', '0008_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
