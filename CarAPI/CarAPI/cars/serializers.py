from datetime import datetime

from rest_framework import serializers

from CarAPI.accounts.serializers import AppUserSerializer
from CarAPI.cars.models import UserCar, CarBrand, CarModel

'''
------------- User Car Serializers -------------
'''


class CarInfoMixin:
    @staticmethod
    def get_car_model_info(obj):
        car_model = obj.car_model

        data = CarModelSerializer(car_model).data
        return data

    @staticmethod
    def get_car_brand_info(obj):
        car_brand = obj.car_brand

        data = CarBrandSerializer(car_brand).data
        return data


class UserCarSerializer(CarInfoMixin, serializers.ModelSerializer):
    user = AppUserSerializer(read_only=True)
    car_model_info = serializers.SerializerMethodField(read_only=True, source='car_model')
    car_brand_info = serializers.SerializerMethodField(read_only=True, source='car_brand')

    class Meta:
        model = UserCar
        fields = ('pk', 'user', 'car_model', 'car_brand', 'car_model_info', 'car_brand_info', 'first_reg', 'odometer')
        extra_kwargs = {
            'car_model': {'label': 'Car Model', 'write_only': True},
            'car_brand': {'label': 'Car Brand', 'write_only': True},
            'car_brand_info': {'hid': False},
            'first_reg': {'label': 'First Registration'},

        }

    @staticmethod
    def get_car_model_info(obj):
        car_model = obj.car_model

        data = CarModelSerializer(car_model).data
        data.pop('car_brand_info')
        data.pop('car_brand')
        return data


class UserCarUpdateSerializer(CarInfoMixin, serializers.ModelSerializer):
    car_model_info = serializers.SerializerMethodField(read_only=True, source='car_model')
    car_brand_info = serializers.SerializerMethodField(read_only=True, source='car_brand')

    class Meta:
        model = UserCar
        fields = ('car_brand', 'car_brand_info', 'car_model', 'car_model_info', 'first_reg', 'odometer')
        extra_kwargs = {
            'car_model': {'label': 'Car Model'},
            'car_brand': {'label': 'Car Brand'},
            'first_reg': {'label': 'First Registration'}
        }

    def update(self, instance, validated_data):
        new_brand = validated_data.get('car_brand', None)
        new_model = validated_data.get('car_model', None)
        new_reg = validated_data.get('first_reg', None)
        new_odometer = validated_data.get('odometer', None)

        if new_brand is not None:
            instance.car_brand = new_brand

        if new_model is not None:
            instance.car_model = new_model

        if new_reg is not None:
            instance.first_reg = new_reg

        if new_odometer is not None:
            instance.odometer = new_odometer

        instance.save()
        return instance

    @staticmethod
    def get_car_model_info(obj):
        car_model = obj.car_model

        data = CarModelSerializer(car_model).data
        data.pop('car_brand_info')
        data.pop('car_brand')
        return data


class UserCarDeleteSerializer(CarInfoMixin, serializers.ModelSerializer):
    car_model_info = serializers.SerializerMethodField(read_only=True, source='car_model')
    car_brand_info = serializers.SerializerMethodField(read_only=True, source='car_brand')

    class Meta:
        model = UserCar
        fields = (
            'pk', 'car_model', 'car_model_info', 'car_brand', 'car_brand_info', 'is_deleted')

    @staticmethod
    def get_car_model_info(obj):
        car_model = obj.car_model

        data = CarModelSerializer(car_model).data
        data.pop('car_brand_info')
        data.pop('car_brand')
        return data


'''
------------- Car Brand Serializers -------------
'''


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('name', 'id', 'created_at', 'deleted_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'deleted_at': {'read_only': True},
        }


class CarBrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('name', 'created_at', 'deleted_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'deleted_at': {'read_only': True},
        }

    def update(self, instance, validated_data):
        new_name = validated_data['name']
        instance.save(name=new_name)
        return instance


'''
------------- Car Model Serializers -------------
'''


class CarModelSerializer(CarInfoMixin, serializers.ModelSerializer):
    car_brand_info = serializers.SerializerMethodField(read_only=True, source='car_brand')

    class Meta:
        model = CarModel
        fields = ('pk', 'name', 'car_brand', 'car_brand_info')
        extra_kwargs = {
            'car_brand': {'label': 'Car Brand'}
        }


class CarModelUpdateSerializer(CarInfoMixin, serializers.ModelSerializer):
    car_brand_info = serializers.SerializerMethodField(read_only=True, source='car_brand')
    update_at = serializers.DateField

    class Meta:
        model = CarModel
        fields = ('name', 'car_brand', 'car_brand_info', 'updated_at')
        extra_kwargs = {
            'car_brand': {'label': 'Car Brand'},
            'updated_at': {'read_only': True}
        }

    def update(self, instance, validated_data):
        new_name = validated_data.get('name', None)
        new_car_brand = validated_data.get('car_brand', None)

        if new_name is not None:
            instance.name = new_name
        if new_car_brand is not None:
            instance.car_brand = new_car_brand
        instance.updated_at = datetime.now().date()
        instance.save()
        return instance


class CarModelDeleteSerializer(CarInfoMixin, serializers.ModelSerializer):
    car_brand_info = serializers.SerializerMethodField(read_only=True, source='car_brand')

    class Meta:
        model = CarModel
        fields = ('id', 'name', 'car_brand', 'car_brand_info', 'created_at', 'updated_at', 'is_deleted')
