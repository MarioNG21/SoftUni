from django.core import validators
from django.db import models

# Create your models here.
from workshop1.petstagram.validators import validate_only_letters, max_size


class Profile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_ASK = 'Do not ask'
    GENDER = [(x, x) for x in (MALE, FEMALE, DO_NOT_ASK)]

    first_name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            validate_only_letters
        )
    )

    last_name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            validate_only_letters
        )
    )

    profile_picture = models.URLField(
        validators=(max_size,)
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )
    e_mail = models.EmailField(
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDER),
        choices=GENDER,
        null=True,
        blank=True,
    )


class Pet(models.Model):
    """
    "Dog", "Bunny", "Parrot", "Fish", or "Other".
    """
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    TYPES = [CAT, DOG, BUNNY, PARROT, FISH, OTHER]
    CHOICES = [(x, x) for x in TYPES]

    name = models.CharField(
        max_length=30,
    )

    type = models.CharField(
        max_length=max(len(x) for x in TYPES),
        choices=CHOICES
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('name', 'user_profile')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            max_size,
        )
    )

    tagged_pets = models.ManyToManyField(Pet)

    description = models.TextField()

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True
    )

    likes = models.IntegerField(
        default=0
    )
