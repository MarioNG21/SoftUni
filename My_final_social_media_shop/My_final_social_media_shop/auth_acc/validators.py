from django.core.exceptions import ValidationError


def age_validate(age):
    if age <= 0:
        raise ValidationError('Age must be greater than zero')
    return None


valid_domain = 'gmail.com'


def gmail_validator(mail):
    _, domain = mail.split('@')
    if domain != valid_domain:
        raise ValidationError('You must enter only gmail emails')
    return None
