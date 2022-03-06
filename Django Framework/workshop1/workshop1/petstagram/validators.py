from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Doesnt consist of alpha characters')


def max_size(max_value):
    def file_size(value):  # add this to some file where you can import it from
        limit = max_value * 1024 * 1024
        if value.size > limit:
            raise ValidationError(f'File too large. Size should not exceed {max_value} MB.')

    return file_size


def validation_year_in_range(year):
    if year not in range(1920, date.today().year + 1):
        raise ValidationError(f"Year must be in range 1920 {date.today().year}")
