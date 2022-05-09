from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from datetime import datetime
from CarAPI.accounts.mixins import AllowAllActionMixin
from CarAPI.cars.models import UserCar, CarBrand, CarModel
from CarAPI.cars.serializers import UserCarSerializer, CarBrandSerializer, CarModelSerializer, CarModelUpdateSerializer, \
    CarModelDeleteSerializer, UserCarUpdateSerializer, UserCarDeleteSerializer


class UserCarIndexAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer

    def get_queryset(self):
        user = self.request.user
        qs = UserCar.objects.filter(user=user)
        if qs.exists():
            return qs
        return UserCar.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer


class UserCarUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserCarUpdateSerializer
    queryset = UserCar.objects.all()

    def get_queryset(self):
        user = self.request.user
        qs = UserCar.objects.filter(user=user)
        if qs.exists():
            return qs
        return UserCar.objects.none()

    def perform_update(self, serializer):
        return super().perform_update(serializer)


class UserCarDeleteAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = UserCarDeleteSerializer
    queryset = UserCar.objects.all()

    def get_queryset(self):
        user = self.request.user
        qs = UserCar.objects.filter(user=user)
        if qs.exists():
            return qs
        return UserCar.objects.none()

    def perform_destroy(self, instance):
        instance.soft_delete()
        instance.deleted_at = datetime.now()
        instance.save()
        return instance


class CarBrandListCreateAPIView(AllowAllActionMixin, generics.ListCreateAPIView):
    serializer_class = CarBrandSerializer
    queryset = CarBrand.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user = self.request.user

        return CarBrand.objects.all()


class CarBrandUpdateAPIView(AllowAllActionMixin, generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_update(self, serializer):
        return super().perform_update(serializer)


class CarBrandDeleteAPIView(AllowAllActionMixin, generics.RetrieveDestroyAPIView):
    lookup_field = 'pk'
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_destroy(self, instance):
        instance.soft_delete()
        instance.deleted_at = datetime.now()
        instance.save()
        return instance


class CarModelListCreateAPIView(AllowAllActionMixin, generics.ListCreateAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class CarModelUpdateAPIView(AllowAllActionMixin, generics.RetrieveUpdateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelUpdateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_update(self, serializer):
        return super().perform_update(serializer)


class CarModelDeleteAPIView(AllowAllActionMixin, generics.RetrieveDestroyAPIView):
    lookup_field = 'pk'
    queryset = CarModel.objects.all()
    serializer_class = CarModelDeleteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_destroy(self, instance):
        instance.soft_delete()

        instance.save()
        return instance
