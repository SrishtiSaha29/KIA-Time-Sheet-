# Generated by Django 4.2.6 on 2023-12-19 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.CharField(max_length=10, null=True)),
                ('password', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, default='pic.png', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
