from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from ws_exercise.auth_accounts.manager import UserManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    MAX_LENGTH_USERNAME = 25

    username = models.CharField(max_length=MAX_LENGTH_USERNAME, unique=True)

    is_staff = models.BooleanField(default=False)

    date_of_join = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    objects = UserManager()


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

    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"
