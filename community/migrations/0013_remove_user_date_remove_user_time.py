# Generated by Django 4.0.4 on 2022-05-25 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0012_user_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='time',
        ),
    ]