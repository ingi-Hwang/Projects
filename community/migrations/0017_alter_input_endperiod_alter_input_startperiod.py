# Generated by Django 4.0.3 on 2022-06-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0016_alter_input_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='endperiod',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='input',
            name='startperiod',
            field=models.DateField(null=True),
        ),
    ]