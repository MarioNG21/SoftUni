# Generated by Django 4.0.2 on 2022-02-19 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='street',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.address'),
        ),
    ]