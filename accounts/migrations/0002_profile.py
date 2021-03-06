# Generated by Django 2.2 on 2019-12-06 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('avatar', models.ImageField(default='', upload_to='projectapp/images')),
                ('year_of_study', models.DateField(default=django.utils.timezone.now)),
                ('preference', models.CharField(choices=[('Web Dev', 'Web Dev'), ('Mobile app dev', 'Mobile app dev'), ('UI/UX', 'UI/UX')], max_length=50)),
                ('skills', models.CharField(choices=[('Node', 'Node'), ('Flutter', 'Flutter'), ('Django', 'Django'), ('Swift', 'Swift'), ('Adobe XD', 'Adobe XD')], max_length=50)),
                ('projects_count', models.IntegerField(default=0)),
                ('manager', models.BooleanField(default=False)),
                ('username', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
