# Generated by Django 5.1.7 on 2025-03-26 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_userprofile_full_name_userprofile_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]
