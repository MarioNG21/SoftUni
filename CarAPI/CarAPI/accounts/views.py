from django.contrib.auth import get_user_model, login
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from CarAPI.accounts.mixins import AllowAllActionMixin
from knox.models import AuthToken
from CarAPI.accounts.serializers import AppUserSerializer, RegisterSerializer, LoginSerializer

UserModel = get_user_model()


class UserListAPIView(generics.ListAPIView):
    serializer_class = AppUserSerializer
    queryset = UserModel.objects.all()


class RegisterAPIView(AllowAllActionMixin, generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return self.request.user

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)[1]

        return Response(
            {'user': AppUserSerializer(user, context=self.get_serializer_context()).data, 'token': token},

        )


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginSerializer(data=data)
        email = data['email']
        if serializer.is_valid(raise_exception=True):
            user = UserModel.objects.filter(email=email).get()
            login(request, user)
            token_qs = user.auth_token_set.all()
            if token_qs.exists():
                token = token_qs.first()
            else:
                token = AuthToken.objects.create(user)[1]
            new_data = serializer.data
            new_data['token'] = token.pk
            return Response(new_data)
        return Response(serializer.errors)
