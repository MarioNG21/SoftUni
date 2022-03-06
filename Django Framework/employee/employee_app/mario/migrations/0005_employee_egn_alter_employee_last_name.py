# Generated by Django 4.0.1 on 2022-01-31 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mario', '0004_alter_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='egn',
            field=models.IntegerField(default=0, unique=True, verbose_name='EGN'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
