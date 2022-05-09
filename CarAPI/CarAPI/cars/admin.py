from django.contrib import admin

from CarAPI.cars.models import CarBrand, CarModel, UserCar


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', 'id')


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'car_brand', 'updated_at',)
    list_display_links = ('name', 'id')


@admin.register(UserCar)
class UserCarAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_reg', 'car_brand', 'deleted_at', 'car_model')
    list_display_links = ('first_reg', 'id')
