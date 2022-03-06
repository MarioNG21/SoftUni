from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def valid_price(value):
    if value < 0:
        raise ValidationError('Price must be more than 0.0')


def username_valid_name(value):
    valid_symbol = '_'
    if valid_symbol in value:
        result = value.replace(valid_symbol, '')
        if result.isalnum():
            return None
        else:
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
    else:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(MinLengthValidator(2),
                    username_valid_name)
    )

    email = models.EmailField()
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_LENGTH = 30

    POP = "Pop Music"
    JAZZ = "Jazz Music"
    RB = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIP_HOP = "Hip Hop Music"
    OTHER = "Other"

    GENRE = [(x, x) for x in (POP, JAZZ, RB, ROCK, COUNTRY, DANCE, HIP_HOP, OTHER)]

    album_name = models.CharField(
        max_length=MAX_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=MAX_LENGTH
    )

    genre = models.CharField(
        max_length=MAX_LENGTH,
        choices=GENRE
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField()
    price = models.FloatField(
        validators=(valid_price,)
    )
