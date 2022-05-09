from django.contrib.auth import get_user_model
from django.db import models

from CarAPI.cars.validators import only_letters_and_nums

UserModel = get_user_model()


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class CarBrand(SoftDeleteModel):
    MAX_CAR_NAME_LENGTH = 50

    name = models.CharField(
        max_length=MAX_CAR_NAME_LENGTH,
        verbose_name='Car Brand'
    )

    created_at = models.DateField(auto_now_add=True)

    deleted_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class CarModel(SoftDeleteModel):
    MAX_LENGTH_NAME = 70

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Car Model'
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True, blank=True)

    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class UserCar(SoftDeleteModel):
    MAX_LENGTH_REG = 25

    first_reg = models.CharField(
        max_length=MAX_LENGTH_REG,
        validators=(only_letters_and_nums,)
    )

    odometer = models.IntegerField(
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE
    )

    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE
    )

    created_at = models.DateField(auto_now_add=True)

    deleted_at = models.DateField(null=True, blank=True)
