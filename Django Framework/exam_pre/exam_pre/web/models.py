from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible

VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE = 'Ensure this value contains only letters.'


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError(VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE)


@deconstructible
class MaxFileSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        file_size = value.file.size
        if file_size > self.__mb_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __mb_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f'Max file size is {self.max_size:.2f} MB'


# Create your models here.
class Profile(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 15

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        ),

    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        ),
    )
    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(MinValueValidator(BUDGET_MIN_VALUE),)
    )

    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeValidator(IMAGE_MAX_SIZE),
        ),

    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Expense(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    image = models.URLField(
        null=True,
        blank=True,
    )

    price = models.FloatField()

    description = models.TextField(
        null=True,
        blank=True,
    )