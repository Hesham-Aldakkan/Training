# Generated by Django 4.0.6 on 2022-08-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]