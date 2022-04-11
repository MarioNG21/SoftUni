from django.core.exceptions import ValidationError


def age_validate(age):
    if age <= 0:
        raise ValidationError('Age must be greater than zero')
    return None
