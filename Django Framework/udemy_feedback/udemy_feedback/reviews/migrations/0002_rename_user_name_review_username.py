# Generated by Django 4.0.2 on 2022-02-25 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user_name',
            new_name='username',
        ),
    ]