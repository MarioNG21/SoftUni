# Generated by Django 4.0.3 on 2022-03-28 20:39

import My_final_social_media_shop.auth_acc.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_acc', '0002_alter_appuser_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], default='Male', max_length=11),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(validators=[My_final_social_media_shop.auth_acc.models.age_validate]),
        ),
    ]
