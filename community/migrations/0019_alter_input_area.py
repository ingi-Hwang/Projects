# Generated by Django 4.0.3 on 2022-06-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0018_alter_input_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='area',
            field=models.CharField(default='', max_length=20),
        ),
    ]