# Generated by Django 4.0.3 on 2022-03-19 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petstagram', '0002_alter_pet_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='app_user',
        ),
    ]
