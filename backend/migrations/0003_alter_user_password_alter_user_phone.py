# Generated by Django 4.0.6 on 2022-08-01 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
