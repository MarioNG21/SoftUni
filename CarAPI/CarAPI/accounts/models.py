from django.db import models
from django.contrib.auth import models as auth_models

from CarAPI.accounts.manager import AppManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,

    )
    first_name = models.CharField(
        max_length=150,
        default='No First Name'

    )
    last_name = models.CharField(
        max_length=150,
        default='No Last Name'
    )
    date_joined = models.DateField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = AppManager()

