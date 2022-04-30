from django.core.exceptions import ValidationError


def only_letters_and_nums(value):
    if not value.isalnum():
        raise ValidationError('Must contain only letters and numbers!')
