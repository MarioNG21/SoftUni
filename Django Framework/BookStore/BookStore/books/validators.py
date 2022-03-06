from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class GreaterThan:
    def __init__(self, max_value):
        self.max_value = max_value

    def __call__(self, value):
        if not value > self.max_value:
            raise ValidationError(f'This {int(self.max_value)} is to small int')
