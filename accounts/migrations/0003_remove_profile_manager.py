# Generated by Django 2.2 on 2019-12-06 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='manager',
        ),
    ]
