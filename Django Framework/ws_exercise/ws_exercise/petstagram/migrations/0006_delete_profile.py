# Generated by Django 4.0.3 on 2022-03-19 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petstagram', '0005_petphoto_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]