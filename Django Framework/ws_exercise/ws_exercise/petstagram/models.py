from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.deconstruct import deconstructible

from ws_exercise.auth_accounts.models import AppUser


@deconstructible
class MaxSizePhoto:
    def __init__(self, max_value):
        self.max_value = max_value

    def __call__(self, value):
        file_size = value.file.size
        if file_size > self.max_value * 1024 * 1024:
            raise ValidationError(f'The file size must not be larger than {self.max_value}')


UserModel = get_user_model()


# Create your models here.
class Profile(models.Model):
    MAX_LENGTH_NAME = 30
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDER = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=(MinLengthValidator(2),)

    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=(MinLengthValidator(2),)
    )

    profile_picture = models.URLField()

    date_of_birth = models.DateField(

        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDER),
        null=True,
        blank=True,
        choices=GENDER
    )

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"


class Pet(models.Model):
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    TYPE = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    name = models.CharField(
        max_length=30
    )

    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPE),
        choices=TYPE
    )

    user = models.ForeignKey(UserModel,
                             on_delete=models.CASCADE)

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ('name', 'user')

    @property
    def age(self):
        return datetime.today().year - self.date_of_birth.year

    def __str__(self):
        return self.name


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(MaxSizePhoto(5),),
        upload_to='mediafiles'
    )

    tagged_pets = models.ManyToManyField(
        Pet
    )

    description = models.TextField(
        null=True,
        blank=True,
    )
    date_time_published = models.DateTimeField(
        auto_now_add=True,

    )

    likes = models.IntegerField(
        default=0,

    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
     )
