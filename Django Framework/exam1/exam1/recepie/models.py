from django.core.exceptions import ValidationError
from django.db import models


def is_separated_by_comma(value):
    list_of_value = value.split(',')
    if len(list_of_value) == 1:
        raise ValidationError('Ingredients must be separated by commas')


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(
        max_length=250,

    )
    time = models.IntegerField()

    def save(self, *args, **kwargs):
        self.ingredients = ' '.join(self.ingredients.split())
        self.ingredients = self.ingredients.replace(' ', ', ')
        super().save(*args, **kwargs)
