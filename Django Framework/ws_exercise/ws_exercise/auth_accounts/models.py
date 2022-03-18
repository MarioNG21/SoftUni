from django.db import models
from django.contrib.auth import models as auth_models

from ws_exercise.auth_accounts.manager import AppManager


class AppUser(auth_models.AbstractBaseUser):
    MAX_LENGTH_USERNAME = 25

    username = models.CharField(max_length=MAX_LENGTH_USERNAME)

    objects = AppManager()



