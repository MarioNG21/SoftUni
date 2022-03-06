# Generated by Django 4.0.1 on 2022-01-31 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0012_alter_employee_options_testmodel_created_on_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.AddField(
            model_name='department',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-27'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='update_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
