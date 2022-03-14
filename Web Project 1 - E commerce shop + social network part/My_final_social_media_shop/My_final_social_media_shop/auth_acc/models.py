from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.
from My_final_social_media_shop.auth_acc.manager import AppUserManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True
    )

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class Profile(models.Model):
    FIRST_NAME_LENGTH = 150
    LAST_NAME_LENGTH = 150

    first_name = models.CharField(
        max_length=FIRST_NAME_LENGTH,

    )

    last_name = models.CharField(
        max_length=LAST_NAME_LENGTH
    )

    profile_picture = models.ImageField(
        upload_to='media/',
        blank=True,
        null=True
    )

    age = models.IntegerField()

    phone = models.IntegerField(
        null=True,
        blank=True,
        validators=(RegexValidator(regex=r'^\+?(?P<phone>(\d{8,15}))$', message='You must enter a valid phone number'),)

    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
        null=False,
        blank=False,
    )

    def get_full_name(self):
        return f"{self.first_name}{self.last_name}"
