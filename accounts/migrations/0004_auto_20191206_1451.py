# Generated by Django 2.2 on 2019-12-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_profile_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='year_of_study',
            field=models.IntegerField(default=1),
        ),
    ]
