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
