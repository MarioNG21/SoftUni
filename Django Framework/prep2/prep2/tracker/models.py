from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.deconstruct import deconstructible


def only_char(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')


def bigger_than_0(value):
    if value < 0:
        raise ValidationError('Must be greater than 0.')


@deconstructible
class MaxSizeFile:
    def __init__(self, max_value):
        self.max_value = max_value

    def __call__(self, value):
        file_size = value.file.size
        if file_size > self.max_value * 1024 * 1024:
            raise ValidationError(f'Max file size is {self.max_value:.2f} MB')


# Create your models here.
class Profile(models.Model):
    MAX_LENGTH = 15
    first_name = models.CharField(
        max_length=MAX_LENGTH,
        validators=(
            MinLengthValidator(2),
            only_char)

    )
    last_name = models.CharField(
        max_length=MAX_LENGTH,
        validators=(
            MinLengthValidator(2),
            only_char
        )
    )

    budget = models.FloatField(default=0,
                               validators=(bigger_than_0,)
                               )

    profile_image = models.ImageField(upload_to='images/',
                                      null=True,
                                      blank=True,

                                      validators=(MaxSizeFile(5),)
                                      )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Expense(models.Model):
    MAX_LENGTH = 30
    title = models.CharField(max_length=MAX_LENGTH)
    expense_image = models.URLField()
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.FloatField()
