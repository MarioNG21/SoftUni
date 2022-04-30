from django.contrib.auth import get_user_model, authenticate

from knox.models import AuthToken
from rest_framework import serializers

UserModel = get_user_model()


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'first_name', 'last_name')


# Register API

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, label='Confirmation Password', write_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'label': 'First Name'},
            'last_name': {'label': 'Last Name'},

        }

    def create(self, validated_data):
        validated_data.pop('password2')
        user = UserModel.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('email', 'password')
        extra_kwargs = {'password': {"write_only": True}}

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError("You entered wrong credentials")

        return data
