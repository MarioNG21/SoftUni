# Generated by Django 4.0.1 on 2022-01-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.IntegerField(choices=[(1, 'Software Developer'), (2, 'QA Engineer'), (3, 'DevOps Specialist')], default=1),
        ),
    ]
