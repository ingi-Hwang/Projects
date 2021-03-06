# Generated by Django 4.0.3 on 2022-06-29 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0012_user_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', '남성'), ('W', '여성')], default='', max_length=2, verbose_name='성별')),
            ],
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurantLatitue',
            new_name='restaurantLatitude',
        ),
        migrations.RenameField(
            model_name='stay',
            old_name='stayLatitue',
            new_name='stayLatitude',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='tourLatitue',
            new_name='tourLatitude',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='cnt',
            new_name='visitCnt',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='value',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='image_file',
        ),
        migrations.AddField(
            model_name='input',
            name='startime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='tag',
            field=models.ManyToManyField(blank=True, to='community.tag'),
        ),
        migrations.AlterField(
            model_name='input',
            name='area',
            field=models.CharField(choices=[('S', '서울'), ('B', '부산')], default='', max_length=20, verbose_name='지역'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tourTime',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='input',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='community.users'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='community.users'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
