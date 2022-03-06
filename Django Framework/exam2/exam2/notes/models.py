from django.db import models


# Create your models here.
class Profile(models.Model):
    MAX_LEN_NAME = 20

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME
    )

    age = models.IntegerField()

    image_url = models.URLField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Note(models.Model):
    MAX_TITLE_LEN = 30
    title = models.CharField(
        max_length=MAX_TITLE_LEN
    )

    image_url = models.URLField()

    content = models.TextField()
