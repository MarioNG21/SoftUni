from django.db import models


# Create your models here.
class Profile(models.Model):
    MAX_LENGTH_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME
    )

    image_url = models.URLField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    MAX_LENGTH = 30
    title = models.CharField(
        max_length=MAX_LENGTH
    )

    description = models.TextField()

    image = models.URLField()
    type = models.CharField(
        max_length=MAX_LENGTH
    )
