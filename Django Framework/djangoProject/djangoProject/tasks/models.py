from django.db import models


# Create your models here.


# Code - first approach

class Task(models.Model):
    title = models.CharField(
        max_length=15,
        null=False
    )

    work = models.CharField(
        max_length=21,
        null=False
    )