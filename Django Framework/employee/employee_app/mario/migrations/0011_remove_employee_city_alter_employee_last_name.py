# Generated by Django 4.0.1 on 2022-01-31 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mario', '0010_remove_employee_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='city',
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]