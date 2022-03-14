# Generated by Django 4.0.1 on 2022-01-31 11:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('employees', '0009_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dead_line', models.DateField(blank=True, null=True)),
                ('employees', models.ManyToManyField(to='employees.Employee')),
            ],
        ),
    ]

