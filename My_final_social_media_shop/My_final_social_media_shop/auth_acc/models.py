from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth import models as auth_models
from My_final_social_media_shop.auth_acc.manager import AppUserManager
from My_final_social_media_shop.auth_acc.validators import age_validate, gmail_validator


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
        validators=(gmail_validator,)
    )

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    date_joined = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class Profile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    CHOICES = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    LEN_CHOICES = max(len(x) for x in (MALE, FEMALE, DO_NOT_SHOW))

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

    age = models.IntegerField(
        validators=(age_validate,)
    )

    phone = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        validators=(RegexValidator(r'^\+?(?P<phone>(\d{8,15}))$', message='You must enter a valid phone number'),)

    )

    gender = models.CharField(
        max_length=LEN_CHOICES,
        choices=CHOICES
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
